import os
from typing import Optional
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


load_dotenv()
ENV = os.getenv("ENV")
__all__ = ["app_configs", "AppConfigs"]


class DataBaseSettings(BaseSettings):
    DATABASE_URL: str
    TEST_DATABASE_URL: str
    SCHEMA: str


class AppConfig(BaseSettings):
    APP_NAME: str = 'Mechanic Finder'
    URI_PREFIX: str = '/api'
    SWAGGER_DOCS_URL: str = URI_PREFIX + '/docs'
    DB: DataBaseSettings = DataBaseSettings()
    ENV: str
    DEBUG: bool = True if ENV in ["development", "test"] else False
    CORS_ALLOWED: list[str] | str = ["http://localhost"]


app_configs = AppConfig()
