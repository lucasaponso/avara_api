from sqlalchemy import Column, String, Float, Integer
from .connect import Base

class user(Base):
    __tablename__ = 'user'
    username = Column(String(255), primary_key=True)
    password = Column(String(255))