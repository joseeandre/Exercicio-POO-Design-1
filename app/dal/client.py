from sqlalchemy.orm import Session
from typing import List
from models.client import Client
import abc


class ABCClientDal():

    @abc.abstractmethod
    def get_clients(self, skip: int = 0, limit: int = 100) -> List[Client]:
        """gets online Authors"""

    @abc.abstractmethod
    def create_client(self, client: Client) -> Client:
        """creates Transaction"""

    @abc.abstractmethod
    def get_client_by_id(self, client_id: int) -> Client:
        """gets Book by id"""


class ClientDal(ABCClientDal):

    def __init__(self, db_session: Session):
        self.db: Session = db_session

    def get_client_by_id(self, client_id: int) -> Client:
        return self.db.query(Client).filter(Client.id == client_id).first()

    def get_clients(self, skip: int = 0, limit: int = 100) -> List[Client]:
        return self.db.query(Client).filter().offset(skip).limit(limit).all()

    def create_client(self, client: Client) -> Client:
        self.db.add(client)
        self.db.commit()
        self.db.refresh(client)
        return client
    
    def delete_client(self, client_id: int):
        self.db.query(Client).filter(Client.id == client_id).delete()
        self.db.commit()
    
    def update_client(self, client: Client) -> Client:
        self.db.merge(client)
        self.db.commit()
        self.db.refresh(client)
        return client
    
    # def delete_user(self, user: User):
    #     self.db.delete(user)
    #     self.db.commit()


    # def update_status(self, user=User) -> User:
    #     self.db.merge(user)
    #     self.db.commit()
    #     self.db.refresh(user)
    #     return user
