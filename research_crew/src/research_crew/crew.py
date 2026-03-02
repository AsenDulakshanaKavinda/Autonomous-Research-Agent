from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from llms import director_model, planner_model, research_model, analyst_model, write_model
from tools import WikipediaSearchTool, ArxivSearchTool
@CrewBase
class ResearchCrew():
    """ResearchCrew crew"""

    agents: list[BaseAgent]
    tasks: list[Task]

    @agent
    def director_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['director_agent'], 
            llm = director_model,
            verbose=True
        )

    @agent
    def planner_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['planner_agent'],
            llm = planner_model,
            verbose=True
        )
    
    @agent
    def researcher_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher_agent'], 
            llm = research_model,
            tools = [WikipediaSearchTool(), ArxivSearchTool()],
            verbose=True
        )

    @agent
    def analyst_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['analyst_agent'],
            llm = analyst_model,
            verbose=True
        )
    
    @agent
    def writer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['writer_agent'],
            llm = write_model,
            verbose=True
        )



    @task
    def director_task(self) -> Task:
        return Task(
            config=self.tasks_config['director_task'],
        )

    @task
    def create_research_plan(self) -> Task:
        return Task(
            config=self.tasks_config['create_research_plan'],
        )
    
    @task
    def gather_information(self) -> Task:
        return Task(
            config=self.tasks_config['gather_information'],
        )

    @task
    def analyst_findings(self) -> Task:
        return Task(
            config=self.tasks_config['analyst_findings'],
        )
    
    @task
    def writer_report(self) -> Task:
        return Task(
            config=self.tasks_config['writer_report'],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the ResearchCrew crew"""


        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
