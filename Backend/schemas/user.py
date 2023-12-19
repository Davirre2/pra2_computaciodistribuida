#aquí hi ha la lògica i validacions i tal
from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    homes: int

class HomeCreate(UserBase):
    pass