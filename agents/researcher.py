from crewai import Agent
from LLMs import research_model
from tools import wikipedia_search_tool, arxiv_search_tool

researcher_agent = Agent(
    role="Information Research Specialist",
    goal="Gather accurate, relevant, and diverse information from available knowledge sources to support the research plan.",
    backstory="You are a skilled researcher with deep experience in discovering reliable information."
        "You extract facts, trends, and supporting data that will later be analyzed for insights.",
    llm=research_model,
    reasoning=True,
    tools=[wikipedia_search_tool, arxiv_search_tool]
)
