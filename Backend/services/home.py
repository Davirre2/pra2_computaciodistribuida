#aquí hi ha les consultes a BD i tal
import pytest
from sqlmodel import Session
#from requests import Session quin dels dos es xd

import schemas.home
import database.database as database
import models.home as home_model
import schemas.home as schemas
from models.tokendata import TokenData
#from sqlmodel import Session, create_engine, select

class home: #TODO ficau mes bonic
    
    def __init__(self, service_session) -> None:
        self.db = service_session

    def get_home_list_by_id(self, Id: int):
        homes = self.db.query(home_model.Home).filter(home_model.Home.id == Id).first()
        return homes
    
    def get_home_list(self):
        homes = self.db.query(home_model.Home).all()
        return homes
    
    def create_home(self, created_home: schemas.HomeCreate): #TODO canvia noms pls
        new_home = home_model.Home(**created_home.dict())
        self.db.add(new_home)
        self.db.commit()
        self.db.refresh(new_home)
        return new_home
    
    def delete_home(self, id: int, data: TokenData):
        home = self.db.query(home_model.Home).filter(home_model.Home.id == id).first()
        if not home.owner_id == data.user_id:
            raise WrongUserException("L'usuari no és el propietari de la casa")
        self.db.delete(home)
        self.db.commit()
        return home
