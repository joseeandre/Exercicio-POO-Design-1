from factories.config import get_settings
from utils.settings import Settings
from fastapi import APIRouter
from typing import List
import json
from fastapi import Request
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, HTTPBearer

from services.author import ABCAuthorService
from services.book import ABCBookService
from services.transaction import ABCTransactionService
from services.client import ABCClientService

from dto.book import BookCreate, Book, BookUpdate
from dto.transaction import Transaction, TransactionCreate, TransactionUpdate
from dto.author import Author, AuthorCreate
from dto.client import Client, ClientCreate, ClientUpdate

from factories.author import get_author_service
from factories.book import get_book_service
from factories.transaction import get_transaction_service
from factories.client import get_client_service


router = APIRouter()

# authors

@router.post("/authors", response_model=Author)
async def create_author(
    author: AuthorCreate,
    service: ABCAuthorService = Depends(get_author_service),
):
    return service.create_author(author=author)


@router.get("/authors", response_model=List[Author])
async def read_authors(
    skip: int = 0, limit: int = 100,
    service: ABCAuthorService = Depends(get_author_service)
):
    return service.get_authors(skip=skip, limit=limit)

# Books

@router.post("/books", response_model=Book)
async def create_book(
    book: BookCreate,
    service: ABCBookService = Depends(get_book_service),
):
    return service.create_book(book=book)


@router.get("/books", response_model=List[Book])
async def read_books(
    skip: int = 0, limit: int = 100,
    service: ABCBookService = Depends(get_book_service)
):
    return service.get_books(skip=skip, limit=limit)

@router.delete("/books/{book_id}")
async def delete_book(
    book_id: int,
    service: ABCBookService = Depends(get_book_service),
):
    service.delete_book(book_id=book_id)

@router.put("/books/{book_id}", response_model=Book)
async def update_book(
    book_id: int,
    book: BookUpdate,
    service: ABCBookService = Depends(get_book_service),
):
    return service.update_book(book=book, book_id=book_id)

# transactions

@router.post("/transactions", response_model=Transaction)
async def create_transaction(
    transaction: TransactionCreate,
    service: ABCTransactionService = Depends(get_transaction_service),
):
    return service.create_transaction(transaction=transaction)

@router.get("/transactions", response_model=List[Transaction])
async def read_transactions(
    skip: int = 0, limit: int = 100,
    service: ABCTransactionService = Depends(get_transaction_service)
):
    return service.get_transactions(skip=skip, limit=limit)

@router.delete("/transactions/{transaction_id}")
async def delete_transaction(
    transaction_id: int,
    service: ABCTransactionService = Depends(get_transaction_service),
):
    service.delete_transaction(transaction_id=transaction_id)

@router.put("/transactions/{transaction_id}", response_model=Transaction)
async def update_transaction(
    transaction_id: int,
    transaction: TransactionUpdate,
    service: ABCTransactionService = Depends(get_transaction_service),
):
    return service.update_transaction(transaction=transaction, transaction_id=transaction_id)

# client

@router.post("/clients", response_model=Client)
async def create_client(
    client: ClientCreate,
    service: ABCClientService = Depends(get_client_service),
):
    return service.create_client(client=client)

@router.get("/clients", response_model=List[Client])
async def read_clients(
    skip: int = 0, limit: int = 100,
    service: ABCClientService = Depends(get_client_service)
):
    return service.get_clients(skip=skip, limit=limit)

@router.delete("/clients/{client_id}")
async def delete_client(
    client_id: int,
    service: ABCClientService = Depends(get_client_service),
):
    service.delete_client(client_id=client_id)

@router.put("/clients/{client_id}", response_model=Client)
async def update_client(
    client_id: int,
    client: ClientUpdate,
    service: ABCClientService = Depends(get_client_service),
):
    return service.update_client(client=client, client_id=client_id)

# @router.post("/login", response_model=dict)
# async def login(
#     request: Request,
#     service: ABCUserService = Depends(get_user_service)
# ):
#     body = await request.body()
#     body_decode = body.decode("utf-8")
#     body_json = json.loads(body_decode)
#     return service.login(email=body_json['email'], password=body_json['password'])


# @router.get("/user", response_model=Student)
# async def get_current_user(
#     token: str = Depends(security),
#     service: ABCUserService = Depends(get_user_service)
# ):
#     return service.get_current_user(token=token)

# # universities


# @router.post("/universities", response_model=University)
# async def create_university(
#     university: UniversityCreate,
#     token: str = Depends(security),
#     service: ABCUniversityService = Depends(get_university_service)
# ):
#     return service.create_university(university=university)


# @router.get("/universities", response_model=List[University])
# async def read_universities(
#     skip: int = 0, limit: int = 100,
#     service: ABCUniversityService = Depends(get_university_service)
# ):
#     return service.get_universities(skip=skip, limit=limit)


# @router.get("/universities/{university_id}", response_model=University)
# async def read_university(
#     university_id: int,
#     service: ABCUniversityService = Depends(get_university_service)
# ):
#     return service.get_university_by_id(university_id=university_id)
# # company


# @router.post("/companies", response_model=Company)
# async def create_company(
#     company: CompanyCreate,
#     token: str = Depends(security),
#     service: ABCCompanyService = Depends(get_company_service)
# ):
#     return service.create_company(company=company)


# @router.get("/companies", response_model=List[Company])
# async def read_companies(
#     skip: int = 0, limit: int = 100,
#     token: str = Depends(security),
#     service: ABCCompanyService = Depends(get_company_service)
# ):
#     return service.get_companies(skip=skip, limit=limit)

# # jobs


# @router.post("/jobs", response_model=Job)
# async def create_job(
#     job: JobCreate,
#     token: str = Depends(security),
#     service: ABCJobService = Depends(get_job_service)
# ):
#     return service.create_job(job=job)


# @router.get("/jobs", response_model=List[Job])
# async def read_jobs(
#     skip: int = 0, limit: int = 100,
#     token: str = Depends(security),
#     service: ABCJobService = Depends(get_job_service)
# ):
#     return service.get_jobs(skip=skip, limit=limit)


# @router.get("/jobs/{job_id}", response_model=Job)
# async def read_job(
#     job_id: int,
#     token: str = Depends(security),
#     service: ABCJobService = Depends(get_job_service)
# ):
#     job = service.get_job(job_id=job_id)
#     if job is None:
#         raise HTTPException(status_code=404, detail="job not found")
#     return job

# # event


# @router.post("/events", response_model=Event)
# async def create_event(
#     event: EventCreate,
#     token: str = Depends(security),
#     service: ABCEventService = Depends(get_event_service)
# ):
#     return service.create_event(event=event)


# @router.get("/events", response_model=List[Event])
# async def read_events(
#     skip: int = 0, limit: int = 100,
#     token: str = Depends(security),
#     service: ABCEventService = Depends(get_event_service)
# ):
#     return service.get_events(skip=skip, limit=limit)


# @router.get("/events/{event_id}", response_model=Event)
# async def read_event(
#     event_id: int,
#     token: str = Depends(security),
#     service: ABCJobService = Depends(get_event_service)
# ):
#     event = service.get_event(event_id=event_id)
#     if event is None:
#         raise HTTPException(status_code=404, detail="event not found")
#     return event

# # file


# @router.post("/files", response_model=File)
# async def create_file(
#     file: FileCreate,
#     token: str = Depends(security),
#     service: ABCFileService = Depends(get_file_service)
# ):
#     return service.create_file(file=file)


# @router.get("/files", response_model=List[File])
# async def read_files(
#     skip: int = 0, limit: int = 100,
#     token: str = Depends(security),
#     service: ABCFileService = Depends(get_file_service)
# ):
#     return service.get_files(skip=skip, limit=limit)


# @router.get("/files/{file_id}", response_model=File)
# async def read_file(
#     file_id: int,
#     token: str = Depends(security),
#     service: ABCFileService = Depends(get_file_service)
# ):
#     file = service.get_file(file_id=file_id)
#     if file is None:
#         raise HTTPException(status_code=404, detail="file not found")
#     return file

# @router.put("/messages/{message_id}", response_model=Message)
# async def edit_message(
#     user: UserCreate,
#     service: ABCStartService = Depends(get_datawarehouse_service)
# ):
#     return service.create_user(user=user)

# @router.delete("/messages/{message_id}")
# async def delete_message(
#     skip: int = 0, limit: int = 100,
#     service: ABCStartService = Depends(get_datawarehouse_service)
# ):
#     return service.get_users(skip=skip, limit=limit)

# @router.get("/users/{user_id}", response_model=User)
# async def read_user(
#     user_id: int,
#     service: ABCStartService = Depends(get_datawarehouse_service)
# ):
#     user = service.get_user(user_id=user_id)
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user


# @router.post("/users/{user_id}/items", response_model=Item)
# async def create_item_for_user(
#     user_id: int, item: ItemCreate,
#     service: ABCStartService = Depends(get_datawarehouse_service)
# ):
#     return service.create_user_item(item=item, user_id=user_id)


# @router.get("/user-items", response_model=List[Item])
# async def read_items(
#     skip: int = 0, limit: int = 100,
#     service: ABCStartService = Depends(get_datawarehouse_service)
# ):
#     return service.get_items(skip=skip, limit=limit)


@router.get("/info")
async def info(settings: Settings = Depends(get_settings)):
    return {
        "app_name": settings.app_name,
    }
