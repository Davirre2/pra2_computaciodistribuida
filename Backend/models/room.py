# class Room:
#     def __init__(self):
#         self.room_name = "room_name"
#         self.room_home = Home()
#         self.room_sensor = "temperature"

#         #AQUÍ ANIRÀ TAULA DE ROOM

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
#from models.home import Home
from database.database import Base

# class Room(Base):
#     __tablename__ = "room"
#     id = Column(Integer, primary_key=True, index=True)
#     room_name = Column(String)
#     room_device_description = Column(String)

#     #room_home_id = Column(String, ForeignKey("Home.id"))
#     rooms_in_home = relationship("Home", back_populates="home.rooms")
