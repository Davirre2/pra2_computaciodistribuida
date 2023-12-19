from fastapi import APIRouter, Depends
import schemas.home as schemas
import services.home as services
import database.database as database
from sqlmodel import Session


router = APIRouter(
    prefix="/home",
    tags=["home"],
    #dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get("/{id}")
async def list_home(id: int):
    print(id)
    #return await services.get_home_list(id, payload)
    return {"id": id,"home_name": "My Home", "home_description": "Description", "home_address": "123 Main St","owner": 1, }

@router.get("/")
async def list_home():
    print("asd")
    #return {"id": "1","home_name": "My Home", "home_description": "Description", "home_address": "123 Main St","owner": 1, }
    db: Session = (database.get_db())
    return await services.get_home_test(db)

@router.post("/new_home")
async def post_home(payload: schemas.HomeList):#que polles va qui
    return await services.put_home(payload)