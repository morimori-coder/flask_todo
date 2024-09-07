from sqlalchemy import Column, Integer, DateTime, NVARCHAR, Boolean
from app.app import db


class Todo(db.Model):
    """
    TODOリストのモデル
    """
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(NVARCHAR(255), nullable=False)
    deadline = Column(DateTime, nullable=True)
    status = Column(Boolean, default=False)
