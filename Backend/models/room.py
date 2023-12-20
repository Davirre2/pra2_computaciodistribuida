from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base
#from models.home import Home

class Room(Base):
    __tablename__ = "room"
    id = Column(Integer, primary_key=True, index=True)
    room_name = Column(String)
    room_device_description = Column(String)

    home_id = Column(Integer, ForeignKey("home.id"), index = True)
    home = relationship("Home", back_populates="rooms")
