from typing import List
from fastapi import APIRouter, Depends
import schemas.user as schemas
import database.database as database
from services.user import UserService


router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)

user_service = UserService(database.db_get())

@router.get("/", response_model=List[schemas.UserList])
def list_user():
    return user_service.get_user_list()

@router.get("/{id}", response_model=List[schemas.UserList])
def get_user_by_id(id: int):
    return user_service.get_user_by_id(id)

@router.post("/")
def post_user(payload: schemas.UserCreate):
    return user_service.create_user(payload)