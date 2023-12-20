import pytest
from sqlmodel import Session
#from requests import Session quin dels dos es xd

import schemas.room
import database.database as database
from models.room import Room
import schemas.room as schemas
from fastapi import FastAPI, Depends
#from sqlmodel import Session, create_engine, select

class room: #TODO ficau mes bonic
    
    def __init__(self, service_session) -> None:
        self.db = service_session

    def get_room_list_by_home_id(self, Id: int):
        rooms = self.db.query(Room).filter(Room.home_id == Id).all()
        return rooms
    
    def get_room_list(self):
        rooms = self.db.query(Room).all()
        return rooms
    
    def create_room(self, created_room: schemas.RoomCreate): #TODO canvia noms pls
        new_room = Room(**created_room.dict())
        self.db.add(new_room)
        self.db.commit()
        self.db.refresh(new_room)
        return new_room
    
    def delete_room(self, id: int):
        room = self.db.query(Room).filter(Room.id == id).first()
        self.db.delete(room)
        self.db.commit()
        return room
    
    # def test_room():
    #     ow = room.User(id=1, email="asd",)
    #     pn = room.Home(id=1, room_name="country", room_description="code", room_address="number", owner="1", rooms="AS")

    #     assert pn.id == 1
    #     assert pn.room_name == 'country'
    #     assert pn.room_description == 'code'
    #     assert pn.room_address == 'number'
    #     assert pn.owner == '1'
    #     return pn

    # def get_room_test(db: Session):
    #     #engine = create_engine("sqlite:///localhost") #nidea
    #     test_user = room.User(email="user@example.com")
    #     test_room = room.Home(room_name="country", room_description="code", room_address="number", owner=test_user)

    #     #create_room(test_room, db)
    #     deb = next(db)
        
    #     deb.add(test_room)
    #     deb.commit()
    #     deb.refresh(test_room)
    #     #rooms = db.query(room.Home).filter(room.Home.id == id).all()
    #     return "rooms"