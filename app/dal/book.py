from sqlalchemy.orm import Session
from typing import List
from models.book import Book
import abc


class ABCBookDal():

    @abc.abstractmethod
    def get_books(self, skip: int = 0, limit: int = 100) -> List[Book]:
        """gets online Authors"""

    @abc.abstractmethod
    def create_book(self, book: Book) -> Book:
        """creates Book"""

    @abc.abstractmethod
    def get_book_by_id(self, book_id: int) -> Book:
        """gets Book by id"""


class BookDal(ABCBookDal):

    def __init__(self, db_session: Session):
        self.db: Session = db_session

    def get_book_by_id(self, book_id: int) -> Book:
        return self.db.query(Book).filter(Book.id == book_id).first()

    def get_books(self, skip: int = 0, limit: int = 100) -> List[Book]:
        return self.db.query(Book).filter().offset(skip).limit(limit).all()

    def create_book(self, book: Book) -> Book:
        self.db.add(book)
        self.db.commit()
        self.db.refresh(book)
        return book
    
    def delete_book(self, book_id: int):
        self.db.query(Book).filter(Book.id == book_id).delete()
        self.db.commit()
    
    def update_book(self, book: Book) -> Book:
        self.db.merge(book)
        self.db.commit()
        self.db.refresh(book)
        return book
    
    # def delete_user(self, user: User):
    #     self.db.delete(user)
    #     self.db.commit()


    # def update_status(self, user=User) -> User:
    #     self.db.merge(user)
    #     self.db.commit()
    #     self.db.refresh(user)
    #     return user
