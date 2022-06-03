from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    author_id: int
    gender: str
    edition: int
    publishing_company: str
    buy_price: float
    sell_price: float


class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str]
    author_id: Optional[int]
    gender: Optional[str]
    edition: Optional[int]
    publishing_company: Optional[str]
    buy_price: Optional[float]
    sell_price: Optional[float]


class Book(BookBase):
    id: int
    tax: Optional[float]

    class Config:
        orm_mode = True