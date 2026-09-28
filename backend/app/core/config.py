from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str  # postgresql+psycopg://user:pass@host/db?sslmode=require
    stripe_secret_key: str = ""
    stripe_webhook_secret: str = ""
    secret_key: str = "change-me"
    environment: str = "local"

settings = Settings()