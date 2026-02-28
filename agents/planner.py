from crewai import Agent
from LLMs import planner_model
from tools import wikipedia_tool

planner = Agent(
    role="Research Strategy Planner",
    goal="Transform the research objective into a structured investigation roadmap by identifying subtopics, key focus areas, and logical research steps.",
    backstory="You are a strategic thinker skilled in designing investigation plans."
        "Your strength lies in turning complex questions into manageable research paths."
        "You ensure no important dimension of the topic is overlooked.",
    llm=planner_model,
)

