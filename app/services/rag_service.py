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

    db = load_vector_db() # load vector DB from Chroma

    retriever = db.as_retriever() # change vector DB to retriever to be used in the chain for find chunks that are relevant to the question

    ollamallm = ChatOllama(
        model=settings.OLLAMA_MODEL,
        base_url="http://host.docker.internal:11434"
    ) #base_url is set to host.docker.internal to allow the container to access the host machine's network

    chain = RetrievalQA.from_chain_type(
        llm=ollamallm,
        retriever=retriever,
        return_source_documents=True # return source documents to be able to show the user where the answer came from
    ) # create chain to answer questions using the retriever and the LLM

    response = chain.invoke({"query": question})

    answer = response['result']

    sources = []

    for doc in response['source_documents']:
        sources.append(
            {
            "source": doc.metadata.get('source', 'Unknown'),
            "page": doc.metadata.get('page', 0) + 1
            }
        )

    return {"answer": answer, "sources": sources}