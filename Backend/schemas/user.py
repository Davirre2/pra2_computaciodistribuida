#aquí hi ha la lògica i validacions i tal
from pydantic import BaseModel, validator
from re import search

class UserBase(BaseModel):
    email: str
    # @validator('email')
    # def emailvalidation(cls, v):
    #     if (search("^[a-zA-Z0-9.!#$%&'+/=?^`{|}~-]+@[a-zA-Z0-9-]+(?:.[a-zA-Z0-9-]+)$",v) is None):
    #         raise ValueError('must be a valid email')
    #     return v

class User(UserBase): #unused prolly
    id: int
    homes: int
    class Config:
        from_attributes = True

class UserCreate(UserBase):
    pass