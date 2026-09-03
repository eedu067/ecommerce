from enum import StrEnum

from pydantic_settings import BaseSettings, SettingsConfigDict


class EnvEnum(StrEnum):
    DEVELOPMENT = "DEVELOPMENT"
    PRODUCTION = "PRODUCTION"


class Config(BaseSettings):
    # Environment
    ENVIRONMENT: EnvEnum = EnvEnum.DEVELOPMENT

    # Application
    PORT: int = 8080
    HOST: str = "localhost"

    # Configuration
    model_config = SettingsConfigDict(
        case_sensitive=True, extra="ignore", env_file=".env"
    )


config: Config = Config()
