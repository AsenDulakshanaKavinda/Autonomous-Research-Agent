from crewai import Task
from agents import planner

create_research_plan = Task(
    description="Break down the research objective into subtopics and create a structured investigation roadmap.",
    expected_output="A step-by-step research plan listing key areas that must be explored.",
    agent=planner
)
