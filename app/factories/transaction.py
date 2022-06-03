from dal.transaction import TransactionDal, ABCTransactionDal
from fastapi import Depends
from factories.db_session import get_db
from sqlalchemy.orm import Session
from services.transaction import TransactionService, ABCTransactionService


def get_transaction_dal(
    db: Session = Depends(get_db)
) -> ABCTransactionDal:
    dal = TransactionDal(db)
    try:
        yield dal
    finally:
        pass


def get_transaction_service(
    dal: ABCTransactionDal = Depends(get_transaction_dal)
) -> ABCTransactionService:
    service = TransactionService(dal)
    try:
        yield service
    finally:
        pass
