from sqlalchemy.orm import Session

from app.db.models import ChatHistory


def save_chat(
        db: Session,
        question: str,
        answer: str
):

    chat = ChatHistory(
        question=question,
        answer=answer
    )

    db.add(chat)

    db.commit()