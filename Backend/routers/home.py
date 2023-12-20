from typing import List
from fastapi import APIRouter, Depends
import schemas.home as schemas
import services.home as services
import database.database as database
from sqlmodel import Session
from fastapi.security import HTTPBearer
from services.authentication import AuthService

from services.home import home


router = APIRouter(
    prefix="/home",
    tags=["home"],
    #dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

home_service = home(database.db_get())
auth_service = AuthService(database.db_get())

@router.get("/{id}")
def list_home(id: int):
    return home_service.get_home_list_by_id(id)

@router.get("/", response_model=List[schemas.HomeList])
def list_home():
    return home_service.get_home_list()

@router.post("/")
def post_home(payload: schemas.HomeCreate):
    return home_service.create_home(payload)

@router.delete("/{id}")
def delete_home(id: int, token = Depends(HTTPBearer())):
    data = auth_service.check_token(token)
    return home_service.delete_home(id, data)