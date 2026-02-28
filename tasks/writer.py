from crewai import Task
from agents import writer

writer_report = Task(
    description="Create a structured research report based on the analyzed insights.",
    expected_output="""    
            A final research report including
            - Executive Summary
            - Key insights
            - Trends
            - Opportunities
            - Risks
            - Future Outlook""",
    agent=writer
)
