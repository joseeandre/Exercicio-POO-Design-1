from dal.book import BookDal, ABCBookDal
from fastapi import Depends
from factories.db_session import get_db
from sqlalchemy.orm import Session
from services.book import BookService, ABCBookService


def get_book_dal(
    db: Session = Depends(get_db)
) -> ABCBookDal:
    dal = BookDal(db)
    try:
        yield dal
    finally:
        pass


def get_book_service(
    dal: ABCBookDal = Depends(get_book_dal)
) -> ABCBookService:
    service = BookService(dal)
    try:
        yield service
    finally:
        pass
