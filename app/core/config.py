from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Runtime configuration loaded from environment variables."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_name: str = "CRICKET LAD"
    app_env: str = "development"
    log_level: str = "INFO"
    vector_store_path: str = "data/vector_store/store.json"
    document_store_path: str = "data/documents"
    top_k: int = Field(default=4, ge=1, le=20)
    openai_api_key: str = ""
    openai_model: str = "gpt-4.1-mini"
    openai_embedding_model: str = "text-embedding-3-small"
    pinecone_api_key: str = ""
    pinecone_index_name: str = "cricket-lad"


@lru_cache
def get_settings() -> Settings:
    return Settings()
