from sqlalchemy import Column, Integer, DateTime, NVARCHAR, Boolean

# from app.db.db_settings import engine
from app.db.db_settings import Base


class Todo(Base):
    """
    TODOリストのモデル
    """
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(NVARCHAR(255), nullable=False)
    deadline = Column(DateTime, nullable=True)
    status = Column(Boolean, default=False)
