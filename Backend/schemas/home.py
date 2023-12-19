#aquí hi ha la lògica i validacions i tal
#la forma eb la que pilla la info el endpint

from pydantic import BaseModel

class HomeBase(BaseModel):
    home_name: str
    rooms: int

class HomeCreate(HomeBase):
    pass

class Home(HomeBase):
    id: int
    owner: int
    rooms: int
    home_description: str
    home_address: str

    class Config:
        from_attributes = True

class HomeList(HomeBase):
    home_name: str
    home_description: str
    home_address: str
    owner: int

# class HomeListUser(BaseModel): #no estic segur
#     home_name: str
#     home_description: str
#     home_address: str