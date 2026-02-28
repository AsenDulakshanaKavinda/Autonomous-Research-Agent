from crewai import Task
from agents import analyst_agent
from .researcher import gather_information

analyst_findings = Task(
    description="Analyze gathered information to extract insights, trends, opportunities, and potential risks.",
    expected_output="A set of meaningful insights derived from the research findings.",
    agent=analyst_agent,
    context=[gather_information]
)
