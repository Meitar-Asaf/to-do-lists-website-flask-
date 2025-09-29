from .base import Base
from sqlalchemy import Column, ForeignKey, Integer, String



class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String, nullable=True)
    todo_list_id = Column(Integer, ForeignKey('todo_lists.id'), nullable=False)