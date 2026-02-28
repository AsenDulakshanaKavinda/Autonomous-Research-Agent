from crewai import Task
from agents import director

director_task = Task(
    description="Conduct a thorough research about AI Agents."
                "Make sure you find any interesting and relevant information given the current year is 2025.",
    expected_output="A clear research objective statement that describes what needs to be investigated.",
    agent=director
)
