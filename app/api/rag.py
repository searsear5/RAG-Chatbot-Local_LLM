from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.database import get_db

from app.schemas.rag import (
    QuestionRequest,
    AnswerResponse
)

from app.services.rag_service import (
    ingest_document,
    ask_question
)

from app.repositories.chat_repository import (
    save_chat
)

router = APIRouter()


@router.post("/upload")
async def upload_pdf(
        file: UploadFile = File(...)
):

    path = f"data/uploads/{file.filename}"

    with open(path, "wb") as f:
        content = await file.read()
        f.write(content)

    ingest_document(path)

    return {
        "message": "Upload success"
    }


@router.post(
    "/ask",
    response_model=AnswerResponse
)
def ask(
        request: QuestionRequest,
        db: Session = Depends(get_db)
):

    answer = ask_question(request.question)

    save_chat(
        db,
        request.question,
        answer
    )

    return {
        "answer": answer
    }