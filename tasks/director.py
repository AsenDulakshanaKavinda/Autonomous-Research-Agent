from crewai import Task
from agents import director_agent

director_task = Task(
    description="Conduct a thorough research about {topic}."
                "Make sure you create a clear research objective statement that describes what needs to be investigated.",
    expected_output="A clear research objective statement that describes what needs to be investigated for planner AI agent.",
    agent=director_agent
)
