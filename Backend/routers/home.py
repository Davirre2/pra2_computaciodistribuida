from fastapi import APIRouter, Depends
import schemas.home as schemas
import services.home as services
import database.database as database
from sqlmodel import Session

from services.home import home


router = APIRouter(
    prefix="/home",
    tags=["home"],
    #dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

home_service = home(database.db_get())

@router.get("/{id}")
def list_home(id: int):
    return home_service.get_home_list_byId(id)

@router.get("/")
def list_home():
    return home_service.get_home_list()

@router.post("/")
def post_home(payload: schemas.HomeCreate):#que polles va qui #no ho sé
    return home_service.create_home(payload)