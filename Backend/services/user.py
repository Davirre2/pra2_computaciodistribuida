#aquí hi ha les consultes a BD i tal
import pytest
from sqlmodel import Session
#from requests import Session quin dels dos es xd

import database.database as database
import schemas.user as schemas
import models.user as user_model

from exceptions.UsedEmailException import UsedEmailException

class UserService: #TODO ficau mes bonic
    
    def __init__(self, service_session) -> None:
        self.db = service_session
    
    def create_user(self, created_user: schemas.UserCreate): #TODO canvia noms pls
        email_check = self.db.query(user_model.User).filter(user_model.User.email == created_user.email).first()
        if email_check is not None:
            raise UsedEmailException("El email ja esta a la base de dades, tonto.")
        new_user = user_model.User(**created_user.dict())
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user
    
    def get_user_list(self):
        users = self.db.query(user_model.User).all()
        return users