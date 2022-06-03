from sqlalchemy.orm import Session
from typing import List
from models.author import Author
import abc


class ABCAuthorDal():

    @abc.abstractmethod
    def get_author_by_email(self, email: str) -> Author:
        """gets Author by name"""

    @abc.abstractmethod
    def get_authors(self, skip: int = 0, limit: int = 100) -> List[Author]:
        """gets online Authors"""

    @abc.abstractmethod
    def create_author(self, author: Author) -> Author:
        """creates Author"""


class AuthorDal(ABCAuthorDal):

    def __init__(self, db_session: Session):
        self.db: Session = db_session

    def get_author_by_email(self, email: str) -> Author:
        return self.db.query(Author).filter(Author.email == email).first()

    def get_authors(self, skip: int = 0, limit: int = 100) -> List[Author]:
        return self.db.query(Author).filter().offset(skip).limit(limit).all()

    def create_author(self, author: Author) -> Author:
        self.db.add(author)
        self.db.commit()
        self.db.refresh(author)
        return author
    
    # def delete_user(self, user: User):
    #     self.db.delete(user)
    #     self.db.commit()


    # def update_status(self, user=User) -> User:
    #     self.db.merge(user)
    #     self.db.commit()
    #     self.db.refresh(user)
    #     return user
