#aquí hi ha la lògica i validacions i tal
#la forma eb la que pilla la info el endpint

from pydantic import BaseModel

class HomeList(BaseModel):
    home_name: str
    home_description: str
    home_address: str
    owner: int

class HomeListUser(BaseModel): #no estic segur
    home_name: str
    home_description: str
    home_address: str