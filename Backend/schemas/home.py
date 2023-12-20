#aquí hi ha la lògica i validacions i tal
#la forma eb la que pilla la info el endpint

from pydantic import BaseModel, validator

class HomeBase(BaseModel):
    home_name: str

class HomeCreate(HomeBase): #post
    home_description: str
    home_address: str
    owner_id: int

class Home(HomeBase):
    id: int
    owner_id: int
    #rooms: int #list[Room] = []
    home_description: str
    home_address: str

    # class Config:
    #     from_attributes = True


class HomeList(HomeBase):
    home_name: str
    home_description: str
    home_address: str
    owner: int

# class HomeListUser(BaseModel): #no estic segur
#     home_name: str
#     home_description: str
#     home_address: str