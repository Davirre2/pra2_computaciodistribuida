from typing import Optional
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped
from typing import List

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
    #rooms_ids = Column(String, ForeignKey("room.id"))
    #rooms = relationship("Room", back_populates="home")  #TODO aixo chatgpt deia que feia falta
    
    rooms: Mapped[List["Room"]] = relationship("Room", back_populates="home")
    owner = relationship("User", back_populates="homes") #maybe?

