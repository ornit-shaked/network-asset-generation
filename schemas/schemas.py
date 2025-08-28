from typing import List, Optional

from pydantic import BaseModel, Field


# Defines a single job posting
class JobPosting(BaseModel):
    """Schema for a single job posting found by the agent."""

    title: str = Field(description="The title of the job posting.")
    company: str = Field(description="The name of the company posting the job.")
    location: str = Field(description="The location of the job.")
    url: Optional[str] = Field(None, description="The URL to the job posting.")
    summary: str = Field(description="A brief summary of the job description.")


# Defines the final, structured response containing a list of job postings
class AgentResponse(BaseModel):
    """Schema for the final agent response, containing a list of job postings."""

    job_postings: List[JobPosting] = Field(
        description="A list of job postings found by the agent."
    )


# from typing import List
#
# from pydantic import BaseModel, Field
#
#
# class Source(BaseModel):
#     """Schema for a source used by the agent"""
#
#     url: str = Field(description="The URL of the source")
#
#
# class AgentResponse(BaseModel):
#     """Schema for agent response with answer and sources"""
#
#     answer: str = Field(description="The agent's answer to the query")
#     sources: List[Source] = Field(
#         default_factory=list, description="List of sources used to generate the answer"
#     )
