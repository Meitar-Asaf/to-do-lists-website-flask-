from .base import Base
from sqlalchemy import Boolean, Column, Integer, String


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    is_staff = Column(Boolean, default=False)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    password = Column(String)