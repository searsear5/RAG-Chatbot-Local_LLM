import json
from sqlalchemy.orm import Session
from app.db.models import ChatHistory


def save_chat(
        db: Session,
        question: str,
        answer: str,
        sources: list
):

    chat = ChatHistory(
        question=question,
        answer=answer,
        sources=json.dumps(sources)
    )

    db.add(chat)
    db.commit()