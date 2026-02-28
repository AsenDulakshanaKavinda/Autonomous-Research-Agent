from crewai import Task
from agents import researcher_agent
from .planner import create_research_plan

gather_information = Task(
    description="Collect relevant information, facts, and knowledge related to the research plan from available sources.",
    expected_output="A summarized collection of key findings and supporting information.",
    agent=researcher_agent,
    context=[create_research_plan]
)
