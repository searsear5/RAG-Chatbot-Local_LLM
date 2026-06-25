from langchain_community.vectorstores import (
    Chroma
)

from app.services.embedding_service import (
    get_embedding
)

from app.core.config import settings


def save_to_vector(chunks):

    embeddings = get_embedding()

    return Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=settings.CHROMA_PATH
    )


def load_vector_db():

    embeddings = get_embedding()

    return Chroma(
        persist_directory=settings.CHROMA_PATH,
        embedding_function=embeddings
    )