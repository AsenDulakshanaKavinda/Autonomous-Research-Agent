from crewai import Agent, Crew, Task, Process
from agents import director_agent, planner_agent, researcher_agent, analyst_agent, writer_agent
from tasks import director_task, create_research_plan, gather_information, analyst_findings, writer_report

crew = Crew(
    agents=[director_agent, planner_agent, researcher_agent, analyst_agent, writer_agent],
    tasks=[director_task, create_research_plan, gather_information, analyst_findings, writer_report],
    verbose=True
)

def result():
    topic = "attention is all you need transformer"
    crew_output = crew.kickoff(
        inputs={"topic": topic}
    )

    print(crew_output)