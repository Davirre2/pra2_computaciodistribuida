#aquí hi ha les consultes a BD i tal
import pytest
from sqlmodel import Session
#from requests import Session quin dels dos es xd

import schemas.home
import database.database as database
import schemas.home as schemas
import models.user as User
from fastapi import FastAPI, Depends

from exceptions.UsedEmailException import UsedEmailException
#from
#from sqlmodel import Session, create_engine, select

class UserService: #TODO ficau mes bonic
    
    def __init__(self, service_session) -> None:
        self.db = service_session
    
    def create_user(self, created_user: schemas.HomeCreate): #TODO canvia noms pls
        email_check = self.db.query(home_model.User).filter(home_model.User.email == created_user.email).first()
        if email_check is not None:
            raise UsedEmailException("El email ja esta a la base de dades, tonto.")
        new_user = home_model.User(**created_user.dict())
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user
    
    def get_user_list(self):
        users = self.db.query(home_model.User).all()
        return users