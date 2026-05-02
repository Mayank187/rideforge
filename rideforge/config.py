from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    # --- Ollama ---
    ollama_base_url: str = "http://localhost:11434"
    chat_model: str = "gemma4:e2b"
    vision_model: str = "gemma4:e2b"
    embed_model: str = "nomic-embed-text"

    # --- Temperatures ---
    planner_temperature: float = 0.7      # creative itinerary generation
    analyst_temperature: float = 0.2      # weather / road analysis — factual
    advisor_temperature: float = 0.5      # gear recommendations
    supervisor_temperature: float = 0.0   # deterministic routing

    # --- LangSmith ---
    langsmith_tracing: bool = Field(default=False, alias="LANGSMITH_TRACING")
    langsmith_endpoint: str = Field(default="https://api.smith.langchain.com", alias="LANGSMITH_ENDPOINT")
    langsmith_project: str = Field(default="rideforge", alias="LANGSMITH_PROJECT")
    langsmith_api_key: str = Field(default="", alias="LANGSMITH_API_KEY")

    # --- External APIs ---
    openweather_api_key: str = Field(default="", alias="OPENWEATHER_API_KEY")
    nominatim_base_url: str = "https://nominatim.openstreetmap.org"
    osrm_base_url: str = "http://router.project-osrm.org"
    open_elevation_base_url: str = "https://api.open-elevation.com"
    overpass_base_url: str = "https://overpass-api.de/api"

    # --- FastAPI ---
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    api_reload: bool = True

    # --- FAISS knowledge base ---
    faiss_index_path: str = "data/ride_knowledge"
    faiss_top_k: int = 5

    # --- Memory / LangGraph Store ---
    langgraph_store_path: str = "data/store"

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8", "populate_by_name": True}


settings = Settings()
