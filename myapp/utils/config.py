from __future__ import annotations

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="../.env",
        env_file_encoding="utf-8",
        extra="ignore"
    )
    qdrant_host: str = Field(default="localhost")
    qdrant_port: int = Field(default=6333)
    qdrant_grpc_port: int = Field(default=6334)
    openai_api_key: str = Field(..., alias="OPENAI_API_KEY")
    openai_model: str = Field(default="gpt-4-turbo")
    ollama_base_url: str = Field(default="http://localhost:11434")
    ollama_embed_model: str = Field(default="mxbai-embed-large")
    ollama_embedding_dim: int = Field(default=1024)
    log_level: str = Field(default="INFO")

    qdrant_collection_conditions: str = Field(default="med_conditions")
    qdrant_collection_symptoms: str = Field(default="med_symptoms")
    qdrant_collection_recommendations: str = Field(default="med_recommendations")


@lru_cache
def get_config() -> Config:
    return Config()


config = get_config()

