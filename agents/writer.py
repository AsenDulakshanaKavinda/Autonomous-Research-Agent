from crewai import Agent
from LLMs import write_model


writer = Agent(
    role="Research Report Writer",
    goal="Gather accurate, relevant, and diverse information from available knowledge sources to support the research plan.",
    backstory="You are a professional communicator who turns complex analysis into readable, well-organized reports. "
        "You ensure the final output is informative, coherent, and impactful.",
    llm=write_model,
)
