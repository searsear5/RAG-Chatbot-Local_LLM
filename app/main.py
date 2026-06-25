from fastapi import FastAPI

from app.api.rag import router
from app.db.database import Base, engine

# สร้าง table ทั้งหมด
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="RAG AI Assistant",
    version="1.0.0"
)

# Register route
app.include_router(
    router,
    prefix="/api/v1/rag",
    tags=["RAG"]
)