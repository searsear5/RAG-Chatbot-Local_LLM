from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import DateTime

from datetime import datetime
from zoneinfo import ZoneInfo
from app.db.database import Base


class Document(Base):

    __tablename__ = "documents"

    id = Column(Integer, primary_key=True)

    filename = Column(String)

    upload_time = Column(
        DateTime,
        default=lambda: datetime.now(ZoneInfo("Asia/Bangkok"))
    )


class ChatHistory(Base):

    __tablename__ = "chat_history"

    id = Column(Integer, primary_key=True)

    question = Column(Text)

    answer = Column(Text)

    sources = Column(Text)

    created_at = Column(
        DateTime,
        default=lambda: datetime.now(ZoneInfo("Asia/Bangkok"))
    )