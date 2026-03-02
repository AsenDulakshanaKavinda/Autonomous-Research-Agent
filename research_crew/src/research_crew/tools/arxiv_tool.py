
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type
import urllib.request
import urllib.parse

class ArxivSearchInput(BaseModel):
    """ Input schema for ArxivSearchTool """
    query: str = Field(..., description="search topic for arXive papers")
    max_results: int = Field(default=3, description="Number of results to fetch")

class ArxivSearchTool(BaseTool):
    name: str = "ArXive Research search tool"
    description: str = "Search academic papers from arXiv based on a topic"
    args_schema: Type[BaseModel] = ArxivSearchInput

    def _run(self, query: str, max_results: int = 3) -> str:
        try:
            encoded_query = urllib.parse.quote(query)

            url = f"http://export.arxiv.org/api/query?search_query=all:{encoded_query}&start=0&max_results={max_results}"

            with urllib.request.urlopen(url) as response:
                data = response.read().decode("utf-8")

            return data
        
        except Exception as e:
            return f"Error fetching arXiv data: {str(e)}"


arxiv_search_tool = ArxivSearchTool()