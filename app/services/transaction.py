from dto.transaction import Transaction, TransactionCreate, TransactionUpdate

from models.transaction import Transaction as TransactionModel

from dal.transaction import ABCTransactionDal

from fastapi import HTTPException, Depends, status
from typing import List
from pydantic import parse_obj_as
import abc
from datetime import datetime
import json

class ABCTransactionService():

    @abc.abstractmethod
    def get_transactions(self, skip: int = 0, limit: int = 100) -> List[Transaction]:
        """gets Transaction"""

    @abc.abstractmethod
    def get_transaction_by_id(self, transaction_id: int) -> Transaction:
        """gets book"""

    @abc.abstractmethod
    def create_transaction(self, transaction: TransactionCreate) -> Transaction:
        """creates book"""

    @abc.abstractmethod
    def delete_transaction(self, transaction_id: int):
        """deletes Book"""

    @abc.abstractmethod
    def update_transaction(self, transaction: TransactionUpdate, transaction_id: int) -> Transaction:
        """updates Book"""

class TransactionService(ABCTransactionService):

    def __init__(self, dw_dal: ABCTransactionDal):
        self.dal: ABCTransactionDal = dw_dal

    def get_transactions(self, skip: int = 0, limit: int = 100) -> List[Transaction]:
        return parse_obj_as(List[Transaction], self.dal.get_transactions(skip, limit))

    def get_transaction_by_id(self, transaction_id: int) -> Transaction:
        transaction = self.dal.get_transaction_by_id(transaction_id)
        return Transaction.from_orm(transaction) if transaction is not None else None

    def create_transaction(self, transaction: TransactionCreate) -> Transaction:
        db_transaction = TransactionModel(**transaction.dict(exclude_unset=True))
        return Transaction.from_orm(self.dal.create_transaction(transaction=db_transaction))

    def delete_transaction(self, transaction_id: int):
        self.dal.delete_transaction(transaction_id)
    
    def update_transaction(self, transaction: TransactionUpdate, transaction_id: int) -> Transaction:
        current_transaction = self.dal.get_transaction_by_id(transaction_id)
        if current_transaction is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="transaction not found",
            )

        for var, value in vars(transaction).items():
            setattr(current_transaction, var, value) if value else None

        return Transaction.from_orm(self.dal.update_transaction(transaction=current_transaction))