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

    ollama serve

    docker compose up -d --build

    docker ps

OPEN SWAGGER
    http://localhost:8000/docs



