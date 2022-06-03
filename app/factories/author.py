from dal.author import AuthorDal, ABCAuthorDal
from fastapi import Depends
from factories.db_session import get_db
from sqlalchemy.orm import Session
from services.author import AuthorService, ABCAuthorService


def get_author_dal(
    db: Session = Depends(get_db)
) -> ABCAuthorDal:
    dal = AuthorDal(db)
    try:
        yield dal
    finally:
        pass


def get_author_service(
    dal: ABCAuthorDal = Depends(get_author_dal)
) -> ABCAuthorService:
    service = AuthorService(dal)
    try:
        yield service
    finally:
        pass
