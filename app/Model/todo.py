from sqlalchemy import Column, Integer, String, DateTime

# from app.db.db_settings import engine
from db.db_settings import Base


class Todo(Base):
    """
    TODOリストのモデル
    """
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(255), nullable=False)
    deadline = Column(DateTime, nullable=True)
    status = Column(String(10), nullable=False, default="未着手")
