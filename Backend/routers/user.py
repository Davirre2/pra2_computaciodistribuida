from fastapi import APIRouter, Depends
import schemas.user as schemas
import database.database as database
from services.user import UserService


router = APIRouter(
    prefix="/user",
    tags=["user"],
    #dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

user_service = UserService(database.db_get())

# @router.get("/{id}")
# def list_home(id: int):
#     return UserService.get_home_list_byId(id)

@router.get("/")
def list_user():
    return user_service.get_user_list()

@router.post("/")
def post_user(payload: schemas.UserCreate):#que polles va qui
    return user_service.create_user(payload)