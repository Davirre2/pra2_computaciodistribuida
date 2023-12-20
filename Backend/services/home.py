#aquí hi ha les consultes a BD i tal
import pytest
from sqlmodel import Session
#from requests import Session quin dels dos es xd

import schemas.home
import database.database as database
import models.home as home_model
import schemas.home as schemas
#from sqlmodel import Session, create_engine, select

class home: #TODO ficau mes bonic
    
    def __init__(self, service_session) -> None:
        self.db = service_session

    def get_home_list_by_id(self, Id: int):
        homes = self.db.query(home_model.Home).filter(home_model.Home.id == Id).all()
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
    
    def test_homee():
        ow = home.User(id=1, email="asd",)
        pn = home.Home(id=1, home_name="country", home_description="code", home_address="number", owner="1", rooms="AS")

        assert pn.id == 1
        assert pn.home_name == 'country'
        assert pn.home_description == 'code'
        assert pn.home_address == 'number'
        assert pn.owner == '1'
        return pn

    def get_home_test(db: Session):
        #engine = create_engine("sqlite:///localhost") #nidea
        test_user = home.User(email="user@example.com")
        test_home = home.Home(home_name="country", home_description="code", home_address="number", owner=test_user)

        #create_home(test_home, db)
        deb = next(db)
        
        deb.add(test_home)
        deb.commit()
        deb.refresh(test_home)
        #homes = db.query(home.Home).filter(home.Home.id == id).all()
        return "homes"