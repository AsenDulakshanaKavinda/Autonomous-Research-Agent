from crewai import Task
from agents import planner_agent
from .director import director_task

create_research_plan = Task(
    description="Break down the research objective into subtopics and create a structured investigation roadmap.",
    expected_output="A step-by-step research plan listing key areas that must be explored for the research agent.",
    agent=planner_agent,
    context=[director_task]
)
