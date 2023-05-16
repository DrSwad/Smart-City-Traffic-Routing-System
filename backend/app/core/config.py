from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    app_name: str = "Smart City Traffic Routing System"
    version: str = "1.0.0"
    debug: bool = True

    database_url: str = "sqlite:///./traffic.db"

    cors_origins: list = ["http://localhost:8080"]

    class Config:
        env_file = ".env"


settings = Settings()
