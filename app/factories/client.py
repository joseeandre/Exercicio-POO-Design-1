from dal.client import ClientDal, ABCClientDal
from fastapi import Depends
from factories.db_session import get_db
from sqlalchemy.orm import Session
from services.client import ClientService
from services.client import ABCClientService


def get_client_dal(
    db: Session = Depends(get_db)
) -> ABCClientDal:
    dal = ClientDal(db)
    try:
        yield dal
    finally:
        pass


def get_client_service(
    dal: ABCClientDal = Depends(get_client_dal)
) -> ABCClientService:
    service = ClientService(dal)
    try:
        yield service
    finally:
        pass
