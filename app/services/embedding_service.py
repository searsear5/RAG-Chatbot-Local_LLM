from langchain_ollama import (
    OllamaEmbeddings
)

from app.core.config import settings


def get_embedding():

    return OllamaEmbeddings(
        model=settings.OLLAMA_EMBEDDING_MODEL, # use embedding model for generate document to vector and  send to vector database
        base_url="http://host.docker.internal:11434"
    )