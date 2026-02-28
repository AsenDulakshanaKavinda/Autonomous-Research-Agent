from crewai import Task
from agents import researcher

gather_information = Task(
    description="Collect relevant information, facts, and knowledge related to the research plan from available sources.",
    expected_output="A summarized collection of key findings and supporting information.",
    agent=researcher
)
