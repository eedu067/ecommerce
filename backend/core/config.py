from enum import StrEnum

from pydantic import PostgresDsn, computed_field
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

    # Database
    POSTGRES_DB: str = "my_db"
    POSTGRES_USER: str = "my_user"
    POSTGRES_PASSWORD: str = "my_password"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432

    @computed_field
    @property
    def DATABASE_URL(self) -> str:
        return str(
            PostgresDsn.build(
                scheme="postgresql+asyncpg",
                host=self.POSTGRES_HOST,
                port=self.POSTGRES_PORT,
                username=self.POSTGRES_USER,
                password=self.POSTGRES_PASSWORD,
                path=self.POSTGRES_DB,
            )
        )

    # Configuration
    model_config = SettingsConfigDict(
        case_sensitive=True, extra="ignore", env_file=".env"
    )


config: Config = Config()
