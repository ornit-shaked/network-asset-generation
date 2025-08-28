import os

from dotenv import load_dotenv
from langchain.agents import AgentExecutor, create_react_agent
from langchain_aws import ChatBedrock
from langchain_core.output_parsers.pydantic import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_tavily import TavilySearch

from prompts.prompt import REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS
from schemas.schemas import AgentResponse

load_dotenv()


def lookup(name: str) -> AgentResponse:

    # --- Verify AWS and Tavily API keys are loaded ---
    aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    aws_region_name = os.getenv("AWS_REGION_NAME")
    tavily_api_key = os.getenv("TAVILY_API_KEY")

    if not all([aws_access_key_id, aws_secret_access_key, aws_region_name]):
        raise ValueError(
            "AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, and AWS_REGION_NAME environment variables must be set for Bedrock."
        )
    if not tavily_api_key:
        raise ValueError(
            "TAVILY_API_KEY environment variable not set. Please set it securely in your .env file or system environment."
        )

    # --- Initialize Tools ---
    tools = [TavilySearch()]

    # --- Initialize LLM ---
    llm = ChatBedrock(
        model_id="anthropic.claude-3-5-sonnet-20240620-v1:0",
        model_kwargs={"temperature": 0},
        region_name=aws_region_name,
    )

    # --- Define the User's Input Query ---
    # This template will generate the actual question string passed to the agent
    user_query_template_str = """search for 3 job postings for an {name} using langchain in the bay area on linkedin and list their details.
                                    Ensure the output is formatted precisely according to the instructions provided."""
    user_query_template = PromptTemplate(
        template=user_query_template_str, input_variables=["name"]
    )

    # --- Initialize Output Parser ---
    output_parser = PydanticOutputParser(pydantic_object=AgentResponse)

    # --- Customize ReAct Prompt with Format Instructions ---
    react_prompt_with_format_instructions = PromptTemplate(
        template=REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS,
        input_variables=["input", "agent_scratchpad", "tool_names"],
        # 'user_query_template' is the placeholder for the user's question
    ).partial(format_instructions=output_parser.get_format_instructions())

    # --- Create Agent ---
    agent = create_react_agent(
        llm=llm, tools=tools, prompt=react_prompt_with_format_instructions
    )

    # --- Create Agent Executor ---
    agent_executor = AgentExecutor(
        agent=agent, tools=tools, verbose=True, handle_parsing_errors=True
    )

    # --- Build the LCEL Chain for Agent Execution and Output Parsing ---
    # 1. Format the user's query into a string
    # 2. Invoke the agent executor with the formatted query
    # 3. Extract the raw 'output' string from the agent's result dictionary
    # 4. Parse the raw output string into the Pydantic AgentResponse object
    chain = (
        # {"input": user_query_template}  # Pass the PromptTemplate to format
        # | user_query_template  # Format the template with actual name
        # 1. Take the input dictionary with {"name": "..."}
        RunnablePassthrough.assign(
            # 2. Format the user_query_template using the 'name' variable
            #    This creates a single string that the agent will use as its 'input'
            input=lambda x: user_query_template.format(name=x["name"])
        )
        | agent_executor  # Run the agent
        | RunnableLambda(
            lambda x: x["output"]
        )  # Extract the 'output' string from agent's dict
        | RunnableLambda(
            lambda x: output_parser.parse(x)
        )  # Parse the string into Pydantic object
    )
    # --- Invoke the Chain ---
    agent_response: AgentResponse = chain.invoke({"name": name})

    return agent_response
