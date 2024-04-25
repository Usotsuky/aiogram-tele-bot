from datetime import date
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from .database import Base


class Question(Base):
    __tablename__ = 'questions'
    id: Mapped[int] = mapped_column(primary_key=True)
    question: Mapped[str]
    data: Mapped[date]

class Answer(Base):
    __tablename__ = 'answers'
    id: Mapped[int] = mapped_column(primary_key=True)
    answer: Mapped[str]
    question_id: Mapped[int] = mapped_column(ForeignKey('questions.id'))