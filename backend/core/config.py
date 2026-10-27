from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "ARGUS Intelligence Engine"
    app_version: str = "1.0.0"
    debug: bool = True

    database_url: str = "sqlite:///./data/argus.db"

    simulation_entities: int = 500
    simulation_events: int = 100

    model_contamination: float = 0.05

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()