# from datetime import date
# from sqlalchemy import Column, DateTime, Integer, String, Boolean
# from database import Base
# from sqlalchemy.orm import deferred

# from sqlalchemy.orm import Mapped

# #AQUÍ ANIRÀ TAULA DE USER

# class User(Base):
#     tablename = 'user'
#     id: int = Column(Integer, primary_key=True, index=True)
#     token: Mapped[str] = deferred(Column(String, default=""))
#     refresh_token: Mapped[str] = deferred(Column(String, default=""))
#     verification_token: Mapped[str] = deferred(Column(String, default=""))
#     rest_password_token: Mapped[str] = deferred(Column(String, default=""))
#     nickname: str = Column(String, unique=True, index=True)
#     password: Mapped[str] = deferred(Column(String))


from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    # hashed_password = Column(String)
    # is_active = Column(Boolean, default=True)

    #homes = relationship("Home", back_populates="home.id") #maybe no es aixi
