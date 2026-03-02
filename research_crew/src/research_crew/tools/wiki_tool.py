import wikipedia
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type

class WikipediaSearchInput(BaseModel):
    """ Input schema for WikipediaSearchTool """
    query: str = Field(..., description="The topic to search for on wikipedia")

class WikipediaSearchTool(BaseTool):
    name: str = "Wikipedia summary tool"
    description: str = "useful for searching for a topic on wikipedia and returning a brief summary"
    args_schema: Type[BaseModel] = WikipediaSearchInput

    def _run(self, query: str) -> str:
        try:
            wikipedia.set_lang("en")
            page = wikipedia.page(title=query, auto_suggest=False)
            return page.content
        except wikipedia.exceptions.DisambiguationError as e:
            return f"The query '{query}' is too ambiguous. Options: {e.options[:5]}."
        except wikipedia.exceptions.PageError:
            return f"No page found for '{query}'."
        except Exception as e:
            return f"an error occurred: {str(e)}."

wikipedia_search_tool = WikipediaSearchTool()