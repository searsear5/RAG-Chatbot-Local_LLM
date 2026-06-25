from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langchain_ollama import ChatOllama

from langchain.chains import RetrievalQA

from app.services.pdf_service import load_pdf

from app.services.vector_service import (
    save_to_vector,
    load_vector_db
)

from app.core.config import settings


def ingest_document(path: str):

    docs = load_pdf(path)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(docs)

    save_to_vector(chunks)


def ask_question(question: str):

    db = load_vector_db()

    retriever = db.as_retriever()

    llm = ChatOllama(
        model=settings.OLLAMA_MODEL
    )

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever
    )

    return chain.run(question)