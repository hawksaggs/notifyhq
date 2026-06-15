from typing import TypedDict

from pydantic_settings import BaseSettings, SettingsConfigDict


class ConfigSummary(TypedDict):
    app_env: str
    app_host: str
    app_port: int
    app_version: str
    log_level: str
    mongodb_db_name: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    app_env: str = "development"
    app_host: str = "0.0.0.0"
    app_port: int = 8000
    app_version: str = "1.0.0"
    api_v1_prefix: str = "/api/v1"
    secret_key: str
    log_level: str = "INFO"
    cors_origins: list[str] = []
    mongodb_url: str
    mongodb_db_name: str = "notifyhq"
    rabbitmq_url: str

    def summary(self) -> ConfigSummary:
        return {
            "app_env": self.app_env,
            "app_host": self.app_host,
            "app_port": self.app_port,
            "app_version": self.app_version,
            "log_level": self.log_level,
            "mongodb_db_name": self.mongodb_db_name,
        }


settings = Settings()
