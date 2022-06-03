from ast import For
from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey, Float
from datetime import datetime
from sqlalchemy.orm import relationship
from dal.dw_database import Base


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)

    books = relationship("Book", back_populates="author")