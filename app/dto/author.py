from typing import Optional, List
from pydantic import BaseModel, validator
from dto.book import Book


class AuthorBase(BaseModel):
    name: str
    email: str

class AuthorCreate(AuthorBase):
    pass


class Author(AuthorBase):
    id: int
    books: Optional[List[Book]]

    class Config:
        orm_mode = True
