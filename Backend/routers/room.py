from fastapi import APIRouter, Depends
import schemas.room as schemas
import services.room as room
import database.database as database
from sqlmodel import Session

router = APIRouter(
    prefix="/room",
    tags=["room"],
    #dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

room_service = room.room(database.db_get())

@router.get("/{id}")
def list_room(id: int):
    return room_service.get_room_list_byId(id)

@router.get("/")
def list_room():
    return room_service.get_room_list()

@router.post("/")
def post_room(payload: schemas.RoomCreate):#que polles va qui
    return room_service.create_room(payload)