from sqlalchemy import Column, String, Float, Integer
from .connect import Base

class books(Base):
    __tablename__ = 'books'
    bookId = Column(Integer, primary_key=True, unique=True)
    author = Column(String(255))
    title = Column(String(255))