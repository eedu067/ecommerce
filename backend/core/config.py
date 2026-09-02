from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):

    # Port
    PORT: int = 8080

    # Configuration
    model_config = SettingsConfigDict(case_sensitive=True, extra="ignore", env_file=".env")


config: Config = Config()
