import os
from crewai import LLM
from dotenv import load_dotenv; load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
light_model = os.getenv("LIGHT_MODEL")
heavy_model = os.getenv("HEAVY_MODEL")

director_model = LLM(
    model=heavy_model,
    temperature=0.2
)

planner_model = LLM(
    model=light_model,
    temperature=0.2
)

research_model = LLM(
    model=heavy_model,
    temperature=0.2
)

analyst_model = LLM(
    model=heavy_model,
    temperature=0.2
)

write_model = LLM(
    model=light_model,
    temperature=0.2
)