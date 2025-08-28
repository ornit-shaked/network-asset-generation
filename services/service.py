from agents.search_agent import lookup as search_agent
from schemas.schemas import AgentResponse, JobPosting


def logic(name: str) -> AgentResponse:
    """
    Manages the core business logic of the application.

    Args:
        name: The job title to search for.

    Returns:
        An AgentResponse object containing a list of structured JobPosting objects.
    """
    # Call the agent's lookup function which now returns a structured Pydantic object
    agent_response: AgentResponse = search_agent(name=name)

    # You can add additional logic here in the future, for example:
    # - Caching the results
    # - Filtering
    # - Saving

    return agent_response


# Example usage (for testing purposes)
if __name__ == "__main__":
    try:
        job_title = "Data Scientist"
        print(f"Executing service logic for job title: {job_title}")

        # Call the logic function and get the structured Pydantic object
        response = logic(name=job_title)

        # Now you can easily access the structured data
        print("\n--- Service Response ---")
        if response.job_postings:
            print(f"Found {len(response.job_postings)} job postings.")
            for i, job in enumerate(response.job_postings):
                print(f"\nJob {i + 1}:")
                print(f"  Title: {job.title}")
                print(f"  Company: {job.company}")
                print(f"  Location: {job.location}")
                print(f"  URL: {job.url}")
                print(f"  Summary: {job.summary[:100]}...")
        else:
            print("No job postings found.")

    except Exception as e:
        print(f"An error occurred in the service layer: {e}")
