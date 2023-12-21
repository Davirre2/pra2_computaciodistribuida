from typing import List
from pydantic import BaseModel
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
    home_description: str
    home_address: str
    rooms: List[RoomList]

class HomeListDescAddr(HomeBase):
    home_description: str | None = None
    home_address: str | None = None

class HomeModify(HomeBase):
    id: int
    home_name: str | None = None
    home_description: str | None = None
    home_address: str | None = None
    #owner_id: int | None = None

from schemas.user import User
class HomeList(HomeBase):
    id: int
    home_name: str
    home_description: str
    home_address: str
    owner: User
    rooms: List[RoomList] 
