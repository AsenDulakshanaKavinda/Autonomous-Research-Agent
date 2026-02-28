import os
from crewai import LLM
from dotenv import load_dotenv; 
load_dotenv()


api_key = os.getenv("GROQ_API_KEY")
light_model = os.getenv("LIGHT_MODEL")
heavy_model = os.getenv("HEAVY_MODEL")

director_model = LLM(
    model=heavy_model,
    provider="groq",
    api_key=api_key,
    temperature=0.2
)

planner_model = LLM(
    model=light_model,
    provider="groq",
    api_key=api_key,
    temperature=0.2
)

research_model = LLM(
    model=heavy_model,
    provider="groq",
    api_key=api_key,
    temperature=0.2
)

analyst_model = LLM(
    model=heavy_model,
    provider="groq",
    api_key=api_key,
    temperature=0.2
)

write_model = LLM(
    model=light_model,
    provider="groq",
    api_key=api_key,
    temperature=0.2
)