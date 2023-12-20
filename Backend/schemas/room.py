from pydantic import BaseModel, validator

class RoomBase(BaseModel):
    room_name: str

class RoomCreate(RoomBase): #post
    room_device_description: str
    home_id: int

class Room(RoomBase):
    id: int
    #room_home_id: int
    room_device_description: str

class RoomList(RoomBase):
    room_device_description: str
    #room_home_id: int