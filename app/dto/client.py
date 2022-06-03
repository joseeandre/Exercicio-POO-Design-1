from typing import Optional, List
from pydantic import BaseModel, validator
from dto.transaction import Transaction


class ClientBase(BaseModel):
    name: str
    email: str

class ClientCreate(ClientBase):
    pass

class ClientUpdate(BaseModel):
    name: Optional[str]
    email: Optional[str]

class Client(ClientBase):
    id: int
    transactions: Optional[List[Transaction]]

    class Config:
        orm_mode = True
