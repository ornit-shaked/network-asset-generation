# powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex" - if uv (Python package and project manager not exist) from windows cmd install following, should be on path
# uv --version - verify it's exist
# uv init - u may need to tell pycharm to work with uv package manager, file->settings->interpreter
# uv add langchain                   # The core LangChain library for building LLM applications.
# uv add langchain-anthropic         # LangChain integration for anthropic models (e.g., GPT).
# uv add python-dotenv               # python-dotenv, used for loading environment variables from a .env file.
# uv add black isort                 # an uncompromising Python code formatter. usage: uv run black .
# uv add langchain-community  # community-contributed LangChain integrations and tools.
# uv add langchainhub         # The clients for accessing pre-built LangChain components from LangChain Hub.
# uv add langchain-ollama     #
# uv add langchain-tavily     # search api, AI based
# uv add flask                # Light python server, http://127.0.0.1:5000
# uv add langchain-aws boto3 pydantic #
