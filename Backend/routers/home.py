from typing import List
from fastapi import APIRouter, Depends, Request
import schemas.home as schemas
from services.home import HomeService
import database.database as database
from fastapi.security import HTTPBearer
from services.authentication import AuthService


router = APIRouter(
    prefix="/home",
    tags=["home"],
    #dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

home_service = HomeService(database.db_get())
auth_service = AuthService(database.db_get())

@router.get("/{id}", response_model=List[schemas.HomeList])
def list_home(id: int):
    return home_service.get_home_list_by_id(id)

@router.get("/owner/{id}", response_model=List[schemas.HomeList])
def list_homes_by_owner(id: int):
    return home_service.get_home_list_by_owner_id(id)

@router.get("/", response_model=List[schemas.HomeList])
def list_home():
    return home_service.get_home_list()

@router.post("/")
def post_home(payload: schemas.HomeCreate):
    return home_service.create_home(payload)

@router.delete("/{id}", dependencies=[Depends(HTTPBearer())])
async def delete_home(id: int, request: Request, credentials: HTTPBearer = Depends()):
    token = (await credentials(request)).credentials
    data = auth_service.check_token(token)
    return home_service.delete_home(id, data)

@router.post("/search", response_model=List[schemas.HomeList])
def search_home(payload: schemas.HomeListDescAddr):
    return home_service.get_home_list_by_addr_or_desc(payload)

@router.put("/{id}", dependencies=[Depends(HTTPBearer())])
async def modify_home(id: int, new_name: str, new_address: str, new_description: str, request: Request, credentials: HTTPBearer = Depends()):
    token = (await credentials(request)).credentials
    data = auth_service.check_token(token)
    return home_service.update_home(id, new_name, new_address, new_description, data)