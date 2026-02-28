from crewai import Agent
from LLMs import analyst_model


analyst = Agent(
    role="Insight and Trend Analyst",
    goal="Transform collected information into meaningful insights by identifying patterns, opportunities, risks, and future implications.",
    backstory="You are an analytical expert who excels at interpreting data and uncovering deeper meaning."
        "Your work converts raw findings into valuable understanding that supports decision-making.",
    llm=analyst_model
)
