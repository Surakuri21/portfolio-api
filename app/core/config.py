from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application configuration via environment variables.
    Pydantic will automatically read from the .env file and validate the types.
    """

    PROJECT_NAME: str = "Surakuri Portfolio API"
    VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"

    # Security / CORS
    ALLOWED_ORIGINS: str = "http://localhost:5173,http://localhost:3000"

    # Pydantic v2 configuration for loading the .env file
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",  # Ignore extra variables in the .env file not defined here
    )

    @property
    def cors_origins(self) -> list[str]:
        """Converts the comma-separated ALLOWED_ORIGINS string into a Python list."""
        return [origin.strip() for origin in self.ALLOWED_ORIGINS.split(",") if origin]


# Instantiate the settings object
settings = Settings()
