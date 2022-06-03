from dto.author import Author, AuthorCreate

from models.author import Author as AuthorModel

from dal.author import ABCAuthorDal

from fastapi import HTTPException, Depends, status
from typing import List
from pydantic import parse_obj_as
import abc
from datetime import datetime
import json

class ABCAuthorService():

    @abc.abstractmethod
    def get_author_by_email(self, email: str) -> Author:
        """gets Author by name"""

    @abc.abstractmethod
    def get_authors(self, skip: int = 0, limit: int = 100) -> List[Author]:
        """gets online Authors"""

    @abc.abstractmethod
    def create_author(self, author: AuthorCreate) -> Author:
        """creates Author"""

class AuthorService(ABCAuthorService):

    def __init__(self, dw_dal: ABCAuthorDal):
        self.dal: ABCAuthorDal = dw_dal

    def get_author_by_email(self, email: str) -> Author:
        author = self.dal.get_author_by_email(email)
        return Author.from_orm(author) if author is not None else None

    def get_authors(self, skip: int = 0, limit: int = 100) -> List[Author]:
        return parse_obj_as(List[Author], self.dal.get_authors(skip, limit))

    def create_author(self, author: AuthorCreate) -> Author:
        current_author = self.dal.get_author_by_email(author.email)
        if current_author:
            raise HTTPException(
                status_code=400, detail="Email already in use"
            )
        db_author = AuthorModel(email=author.email, name=author.name)
        return Author.from_orm(self.dal.create_author(author=db_author))