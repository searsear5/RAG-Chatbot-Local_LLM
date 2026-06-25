from langchain_ollama import (
    OllamaEmbeddings
)

from app.core.config import settings


def get_embedding():

    return OllamaEmbeddings(
        model=settings.OLLAMA_MODEL
    )