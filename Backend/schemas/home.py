#aquí hi ha la lògica i validacions i tal
#la forma eb la que pilla la info el endpint

from typing import List
from pydantic import BaseModel, validator, field_serializer

from schemas.user import User
from schemas.room import RoomList

class HomeBase(BaseModel):
    pass

class HomeCreate(HomeBase): #post
    home_name: str
    home_description: str
    home_address: str
    owner_id: int

class Home(HomeBase):
    home_name: str
    id: int
    owner_id: int
    #rooms: int #list[Room] = []
    home_description: str
    home_address: str

    # class Config:
    #     from_attributes = True

class HomeListDescAddr(HomeBase):
    home_description: str | None = None
    home_address: str | None = None

class HomeList(HomeBase):
    home_name: str
    home_description: str
    home_address: str
    owner: User
    rooms: List[RoomList] 

    # @field_serializer(owner)
    # def serialize_owner(self, owner: User, _info):
    #     return owner.