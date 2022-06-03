from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from dto.book import Book

class TransactionBase(BaseModel):
    quantity: int
    book_id: int
    client_id: int
    price: float

class TransactionCreate(TransactionBase):
    pass

class TransactionUpdate(BaseModel):
    quantity: Optional[int]
    book_id: Optional[int]
    client_id: Optional[int]
    price: Optional[float]

class Transaction(TransactionBase):
    id: int
    book: Optional[Book]

    class Config:
        orm_mode = True
