from pydantic import BaseModel, validator
from re import search
from typing import List

class UserBase(BaseModel):
    email: str

class User(UserBase): #unused prolly
    id: int

class UserCreate(UserBase):
    password: str
    pass

from schemas.home import Home
class UserList(UserBase):
    id: int
    token: str | None = None
    homes: List[Home]