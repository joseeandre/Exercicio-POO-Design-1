from ast import For
from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey, Float
from datetime import datetime
from sqlalchemy.orm import relationship
from dal.dw_database import Base
from models.author import Author


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    gender = Column(String)
    edition = Column(Integer)
    publishing_company = Column(String)
    buy_price = Column(Float)
    sell_price = Column(Float)
    tax = Column(Float)

    author_id = Column(Integer, ForeignKey(Author.id))

    author = relationship(Author)