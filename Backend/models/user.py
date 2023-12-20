from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped
from typing import List

from database.database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    token = Column(String) #contindrà l'userID i el mail codificat //// jsonWebTokens
    password = Column(String)
    is_active = Column(Boolean, default=True)

    homes: Mapped[List["Home"]] = relationship("Home", back_populates="owner")
