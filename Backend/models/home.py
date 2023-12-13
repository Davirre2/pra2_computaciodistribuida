from typing import Optional
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database.database import Base

class Home(Base):
    __tablename__ = "home"
    id = Column(Integer, primary_key=True, index=True)
    home_name = Column(String)
    home_address = Column(String)
    home_description = Column(String)
    owner = Column(Integer, ForeignKey("user.id"))

    rooms = relationship("Room", back_populates="room.id")
    #owner = relationship("owner", back_populates="home") #maybe?
