from dto.book import Book, BookCreate, BookUpdate

from models.book import Book as BookModel

from dal.book import ABCBookDal

from fastapi import HTTPException, Depends, status
from typing import List
from pydantic import parse_obj_as
import abc
from datetime import datetime
import json

class ABCBookService():

    @abc.abstractmethod
    def get_books(self, skip: int = 0, limit: int = 100) -> List[Book]:
        """gets book"""

    @abc.abstractmethod
    def get_book_by_id(self, book_id: int) -> Book:
        """gets book"""

    @abc.abstractmethod
    def create_book(self, book: BookCreate) -> Book:
        """creates book"""

    @abc.abstractmethod
    def delete_book(self, book_id: int):
        """deletes Book"""

    @abc.abstractmethod
    def update_book(self, book: BookCreate, book_id: int) -> Book:
        """updates Book"""

class BookService(ABCBookService):

    def __init__(self, dw_dal: ABCBookDal):
        self.dal: ABCBookDal = dw_dal

    def get_books(self, skip: int = 0, limit: int = 100) -> List[Book]:
        return parse_obj_as(List[Book], self.dal.get_books(skip, limit))

    def get_book_by_id(self, book_id: int) -> Book:
        book = self.dal.get_book_by_id(book_id)
        return Book.from_orm(book) if book is not None else None

    def create_book(self, book: BookCreate) -> Book:
        tax=0
        if (book.gender == "drama"):
            tax = 0.2*(book.sell_price - book.buy_price)
        db_book = BookModel(**book.dict(exclude_unset=True), tax=tax)
        return Book.from_orm(self.dal.create_book(book=db_book))

    def delete_book(self, book_id: int):
        self.dal.delete_book(book_id)
        return "Excluido com sucesso"
    
    def update_book(self, book: BookUpdate, book_id: int) -> Book:
        current_book = self.dal.get_book_by_id(book_id)
        if current_book is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Book not found",
            )

        for var, value in vars(book).items():
            setattr(current_book, var, value) if value else None
        
        if current_book.gender == "drama":
            tax = 0.2*(current_book.sell_price - current_book.buy_price)
            setattr(current_book, "tax", tax)

        return Book.from_orm(self.dal.update_book(book=current_book))