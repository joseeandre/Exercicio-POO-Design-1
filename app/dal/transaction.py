from sqlalchemy.orm import Session
from typing import List
from models.transaction import Transaction
import abc


class ABCTransactionDal():

    @abc.abstractmethod
    def get_transactions(self, skip: int = 0, limit: int = 100) -> List[Transaction]:
        """gets online Authors"""

    @abc.abstractmethod
    def create_transaction(self, transaction: Transaction) -> Transaction:
        """creates Transaction"""

    @abc.abstractmethod
    def get_transaction_by_id(self, transaction_id: int) -> Transaction:
        """gets Book by id"""


class TransactionDal(ABCTransactionDal):

    def __init__(self, db_session: Session):
        self.db: Session = db_session

    def get_transaction_by_id(self, transaction_id: int) -> Transaction:
        return self.db.query(Transaction).filter(Transaction.id == transaction_id).first()

    def get_transactions(self, skip: int = 0, limit: int = 100) -> List[Transaction]:
        return self.db.query(Transaction).filter().offset(skip).limit(limit).all()

    def create_transaction(self, transaction: Transaction) -> Transaction:
        self.db.add(transaction)
        self.db.commit()
        self.db.refresh(transaction)
        return transaction
    
    def delete_transaction(self, transaction_id: int):
        self.db.query(Transaction).filter(Transaction.id == transaction_id).delete()
        self.db.commit()
    
    def update_transaction(self, transaction: Transaction) -> Transaction:
        self.db.merge(transaction)
        self.db.commit()
        self.db.refresh(transaction)
        return transaction
    
    # def delete_user(self, user: User):
    #     self.db.delete(user)
    #     self.db.commit()


    # def update_status(self, user=User) -> User:
    #     self.db.merge(user)
    #     self.db.commit()
    #     self.db.refresh(user)
    #     return user
