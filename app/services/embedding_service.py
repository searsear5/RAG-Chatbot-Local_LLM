from langchain_ollama import (
    OllamaEmbeddings
)

from app.core.config import settings


def get_embedding():

    return OllamaEmbeddings(
        model=settings.OLLAMA_EMBEDDING_MODEL,
        base_url="http://host.docker.internal:11434"
    )