from ast import For
from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey, Float
from datetime import datetime
from sqlalchemy.orm import relationship
from dal.dw_database import Base
from models.book import Book
from models.client import Client


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    price = Column(Float)
    quantity = Column(Integer)

    book_id = Column(Integer, ForeignKey(Book.id))
    client_id = Column(Integer, ForeignKey(Client.id))

    book = relationship(Book)
    client = relationship(Client)