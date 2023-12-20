from typing import Optional
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped
from typing import List
from database.database import Base

class Home(Base):
    __tablename__ = "home"
    id = Column(Integer, primary_key=True, index=True)
    home_name = Column(String)
    home_address = Column(String)
    home_description = Column(String)
    owner_id = Column(Integer, ForeignKey("user.id"))
    
    rooms: Mapped[List["Room"]] = relationship("Room", back_populates="home")
    owner = relationship("User", back_populates="homes")
