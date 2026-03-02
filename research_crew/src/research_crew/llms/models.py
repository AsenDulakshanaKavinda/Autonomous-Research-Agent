import os
from crewai import LLM
from dotenv import load_dotenv; 
load_dotenv()


groq_api_key = os.getenv("GROQ_API_KEY")
mistral_api_key = os.getenv("MISTRAL_API_KEY")
groq_light_model = os.getenv("GROQ_LIGHT_MODEL")
groq_heavy_model = os.getenv("GROQ_HEAVY_MODEL")
mistral_light_model = os.getenv("MISTRAL_LIGHT_MODEL")
mistral_heavy_model = os.getenv("MISTRAL_HEAVY_MODEL")

director_model = LLM(
    model=groq_heavy_model,
    provider="groq",
    api_key=groq_api_key,
    temperature=0.2
)

planner_model = LLM(
    model=groq_light_model,
    provider="groq",
    api_key=groq_api_key,
    temperature=0.2
)

research_model = LLM(
    model=mistral_heavy_model,
    provider="mistral",
    api_key=mistral_api_key,
    temperature=0.2
)

analyst_model = LLM(
    model=mistral_heavy_model,
    provider="mistral",
    api_key=mistral_api_key,
    temperature=0.2
)

write_model = LLM(
    model=mistral_light_model,
    provider="mistral",
    api_key=mistral_api_key,
    temperature=0.2
)