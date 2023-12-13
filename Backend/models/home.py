from typing import Optional

from sqlmodel import Field, SQLModel

# class Home(SQLModel):
#     def __init__(self):
#         self.home_name = "home_name"
#         self.home_address = "random_address"
#         self.home_description = "ella passa pel bloc"
#         self.owner = "userID"

# class Home(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True, index=True)
#     home_name: str
#     home_address = str
#     home_description: str #es opcional pk si
#     owner: str

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from Backend.database.database import Base

class Home(Base):
    __tablename__ = "home"
    id = Column(Integer, primary_key=True, index=True)
    home_name = Column(String)
    home_address = Column(String)
    home_description = Column(String)
    owner = Column(Integer, ForeignKey("user.id"))

    rooms = relationship("Room", back_populates="room.id")
    #owner = relationship("owner", back_populates="home") #maybe?
