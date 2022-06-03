from dto.client import Client, ClientCreate, ClientUpdate

from models.client import Client as ClientModel

from dal.client import ABCClientDal

from fastapi import HTTPException, Depends, status
from typing import List
from pydantic import parse_obj_as
import abc
from datetime import datetime
import json

class ABCClientService():

    @abc.abstractmethod
    def get_clients(self, skip: int = 0, limit: int = 100) -> List[Client]:
        """gets client"""

    @abc.abstractmethod
    def get_client_by_id(self, client_id: int) -> Client:
        """gets book"""

    @abc.abstractmethod
    def create_client(self, client: ClientCreate) -> Client:
        """creates book"""

    @abc.abstractmethod
    def delete_client(self, client_id: int):
        """deletes Book"""

    @abc.abstractmethod
    def update_client(self, client: ClientUpdate, client_id: int) -> Client:
        """updates Book"""

class ClientService(ABCClientService):

    def __init__(self, dw_dal: ABCClientDal):
        self.dal: ABCClientDal = dw_dal

    def get_clients(self, skip: int = 0, limit: int = 100) -> List[Client]:
        return parse_obj_as(List[Client], self.dal.get_clients(skip, limit))

    def get_client_by_id(self, client_id: int) -> Client:
        client = self.dal.get_client_by_id(client_id)
        return Client.from_orm(client) if client is not None else None

    def create_client(self, client: ClientCreate) -> Client:
        db_client = ClientModel(**client.dict(exclude_unset=True))
        return Client.from_orm(self.dal.create_client(client=db_client))

    def delete_client(self, client_id: int):
        self.dal.delete_client(client_id)
    
    def update_client(self, client: ClientUpdate, client_id: int) -> Client:
        current_client = self.dal.get_client_by_id(client_id)
        if current_client is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="client not found",
            )

        for var, value in vars(client).items():
            setattr(current_client, var, value) if value else None

        return Client.from_orm(self.dal.update_client(client=current_client))