from typing import Optional
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database.database import Base

# from models.room import Room
# from models.user import User

#TODO podriem ficarho dins d'un sol archiu tots el models maybe? de moment estan tots aqui per testing
class Home(Base):
    __tablename__ = "home"
    id = Column(Integer, primary_key=True, index=True)
    home_name = Column(String)
    home_address = Column(String)
    home_description = Column(String)
    owner_id = Column(Integer, ForeignKey("user.id"))
    rooms_ids = Column(String, ForeignKey("room.id"))
    #rooms = relationship("Room", back_populates="home")  #TODO aixo chatgpt deia que feia falta
    
    rooms = relationship("Room", back_populates="rooms_in_home")
    owner = relationship("User", back_populates="homes") #maybe?

class Room(Base):
    __tablename__ = "room"
    id = Column(Integer, primary_key=True, index=True)
    room_name = Column(String)
    room_device_description = Column(String)

    #room_home_id = Column(String, ForeignKey("Home.id"))
    rooms_in_home = relationship("Home", back_populates="rooms")

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    # hashed_password = Column(String)
    # is_active = Column(Boolean, default=True)

    homes = relationship("Home", back_populates="owner") #maybe no es aixi