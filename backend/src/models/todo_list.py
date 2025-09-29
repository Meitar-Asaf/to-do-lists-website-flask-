from .base import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String


class TodoList(Base):
    __tablename__ = 'todo_lists'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
