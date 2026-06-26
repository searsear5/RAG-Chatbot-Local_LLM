System Architecture
User
  │
  ▼
FastAPI API
  │
  ├── Upload PDF
  │       │
  │       ▼
  │   PDF Loader
  │       │
  │       ▼
  │   Text Splitter
  │       │
  │       ▼
  │   Embedding Model
  │       │
  │       ▼
  │   ChromaDB
  │
  └── Ask Question
          │
          ▼
     Retriever
          │
          ▼
      Ollama LLM
          │
          ▼
     Generated Answer
          │
          ▼
    PostgreSQL History


ฺBUILD AND START
    docker compose up -d --build

    docker ps
OPEN SWAGGER
    http://localhost:8000/docs

OLLAMA
    http://host.docker.internal:11434



ตอนนี้อาจแก้ให้ fastAPI กลับไปรันบนเครื่องไม่อยู่บน container
    uvicorn app.main:app --reload