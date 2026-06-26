from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    DATABASE_URL: str

    OLLAMA_MODEL: str

    CHROMA_PATH: str

    OLLAMA_EMBEDDING_MODEL: str

    class Config:
        env_file = ".env"


settings = Settings()