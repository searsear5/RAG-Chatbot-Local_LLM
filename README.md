Upload Flow
User -> /upload -> Load PDF -> Chunking -> Embedding(generate vector) -> Chroma DB(store in vector_db)

Question Flow
User -> /ask -> RetrievalQA(calls Vector Search (retriever),LLM ) -> Retriever (Vector Search in Chroma) -> LLM (Ollama - llama3.2) -> Generated Answer -> return (answer,sources)

Save History
Answer + Sources -> PostgreSQL (chat_history)

ฺBUILD AND START

    ollama serve

    docker compose up -d --build

    docker ps

OPEN SWAGGER
    http://localhost:8000/docs



