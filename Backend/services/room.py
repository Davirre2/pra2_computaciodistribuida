import schemas.room
from models.room import Room
from models.home import Home
import schemas.room as schemas

from exceptions.EmptyResponseException import EmptyResponseException
from exceptions.NonexistentIdException import NonexistentIdException

class RoomService:
    
    def __init__(self, service_session) -> None:
        self.db = service_session

    def get_room_list_by_home_id(self, Id: int):
        rooms = self.db.query(Room).filter(Room.home_id == Id).all()
        if not rooms:
            raise EmptyResponseException("Aquesta casa no te cap habitació assignada")
        return rooms
    
    def get_room_list(self):
        rooms = self.db.query(Room).all()
        if not rooms:
            raise EmptyResponseException("No hi han habitacions a la BBDD")
        return rooms
    
    def create_room(self, created_room: schemas.RoomCreate):
        new_room = Room(**created_room.dict())
        home = self.db.query(Home).filter(Home.id == new_room.home_id).all()
        if not home:
            raise NonexistentIdException("La casa a la que li vols ficar la casa no existeix.")
        self.db.add(new_room)
        self.db.commit()
        self.db.refresh(new_room)
        return new_room
    
    def delete_room(self, id: int):
        room = self.db.query(Room).filter(Room.id == id).first()
        if not room:
            raise NonexistentIdException("L'habitació que vols borrar no existeix")
        self.db.delete(room)
        self.db.commit()
        return room