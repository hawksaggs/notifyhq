from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    app_env: str = "development"
    app_host: str = "0.0.0.0"
    app_port: int = 8000
    api_v1_prefix: str = "/api/v1"
    secret_key: str
    log_level: str = "INFO"
    cors_origins: list[str] = []
    mongodb_url: str
    mongodb_db_name: str = "notifyhq"
    rabbitmq_url: str


settings = Settings()
