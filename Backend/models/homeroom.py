from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base

class Homeroom(Base):
    __tablename__ = "Homeroom"
    home_id = Column(Integer, ForeignKey("home.id"), primary_key = True) #Casa a la que pertany una room
    room_ids = Column(String, ForeignKey("room.id"), primary_key = True) #Rooms que té una casa
