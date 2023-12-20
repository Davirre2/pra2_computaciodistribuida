from fastapi import APIRouter, Depends
import schemas.room as schemas
from services.room import RoomService
import database.database as database
from sqlmodel import Session

router = APIRouter(
    prefix="/room",
    tags=["room"],
    responses={404: {"description": "Not found"}},
)

room_service = RoomService(database.db_get())

@router.get("/{id}")
def list_room(id: int):
    return room_service.get_room_list_by_home_id(id)

@router.get("/")
def list_room():
    return room_service.get_room_list()

@router.post("/")
def post_room(payload: schemas.RoomCreate):
    return room_service.create_room(payload)

@router.delete("/{id}")
async def delete_room(id: int):
    return room_service.delete_room(id)