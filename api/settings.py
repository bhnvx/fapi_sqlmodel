import secrets

from pydantic import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str = secrets.token_urlsafe(32)

    class Config:
        case_sensitive = True


settings = Settings()
