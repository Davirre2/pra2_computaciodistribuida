from exceptions.WrongUserException import WrongUserException
from models.home import Home
from models.user import User
from sqlalchemy.orm import aliased
import schemas.home as schemas
from models.tokendata import TokenData

from exceptions.EmptyPayloadException import EmptyPayloadException
from exceptions.EmptyResponseException import EmptyResponseException
from exceptions.NonexistentIdException import NonexistentIdException

class HomeService:
    
    def __init__(self, service_session) -> None:
        self.db = service_session

    def get_home_list_by_id(self, Id: int):
        home = self.db.query(Home).filter(Home.id == Id).all()
        if not home:
            raise EmptyResponseException("Aquesta casa no existeix")
        return home
    
    def get_home_list_by_owner_id(self, Id: int):
        homes = self.db.query(Home).filter(Home.owner_id == Id).all()
        if not homes:
            raise EmptyResponseException("Aquest usuari no te cap casa")
        return homes
    
    def get_home_list(self):
        homes = self.db.query(Home).all()
        if not homes:
            raise EmptyResponseException("No hi ha cap casa a la BBDD")
        return homes
    
    def create_home(self, created_home: schemas.HomeCreate):
        new_home = Home(**created_home.dict()) 
        owner = self.db.query(User).filter(User.id == new_home.owner_id).all()
        if not owner:
            raise WrongUserException("L'usuari al que estas asignant la casa no exiteix")
        self.db.add(new_home)
        self.db.commit()
        self.db.refresh(new_home)
        return new_home
    
    def delete_home(self, id: int, data: TokenData):
        home = self.db.query(Home).filter(Home.id == id).first()
        if not home:
            raise NonexistentIdException("La casa que estas intentant modificar no existeix")
        if not home.owner_id == data.user_id:
            raise WrongUserException("L'usuari no és el propietari de la casa")
        self.db.delete(home)
        self.db.commit()
        return home
    
    def update_home(self, payload: schemas.HomeModify, data: TokenData):
        id, new_name  = payload.id, payload.home_name
        new_address, new_description = payload.home_address, payload.home_description
        
        home = self.db.query(Home).filter(Home.id == id).first()   #TODO: tractar si no existeix el id de home i que a vegades rebenta sembla?¿
        if not home:
            raise NonexistentIdException("La casa que estas intentant modificar no existeix")
        
        if not home.owner_id == data.user_id:
            raise WrongUserException("L'usuari no és el propietari de la casa")
        
        if home.home_name is not  new_name and new_name is not None:
            self.db.query(Home).filter(Home.id == id).update({Home.home_name: new_name}, synchronize_session = False)
        if home.home_address is not  new_address and new_address is not None:
            self.db.query(Home).filter(Home.id == id).update({Home.home_address: new_address}, synchronize_session = False)
        if home.home_description is not  new_description and new_description is not None:
            self.db.query(Home).filter(Home.id == id).update({Home.home_description: new_description}, synchronize_session = False)
        # if home.owner.id is not  new_owner_id and new_owner_id is not None:
        #     new_owner = aliased(self.db.query(User).filter(User.id == new_owner_id))
        #     self.db.query(Home).filter(Home.id == id).update({Home.owner: new_owner}, synchronize_session = False)
        self.db.commit()
        home = self.db.query(Home).filter(Home.id == id).first()
        return home
        
    def get_home_list_by_addr_or_desc(self, payload: schemas.HomeListDescAddr):
        if payload.home_address is None and payload.home_description is None:
            raise EmptyPayloadException("Hi ha d'haver > 1 valor.")
        
        filterdesc = payload.home_description
        filteraddr = payload.home_address

        if not (filterdesc is None) and not (filteraddr is None):
            list_homes = self.db.query(Home).filter(Home.home_description.ilike(f'%{filterdesc}%') | Home.home_address.ilike(f'%{filteraddr}%')).all()
        elif not (filteraddr is None):
            list_homes = self.db.query(Home).filter(Home.home_address.ilike(f'%{filteraddr}%')).all()
        elif not (filterdesc is None):
            list_homes = self.db.query(Home).filter(Home.home_address.ilike(f'%{filterdesc}%')).all()
        
        if not list_homes:
            raise EmptyResponseException("No hi ha cap casa a la BBDD amb la descripcio que has donat")
        
        return list_homes
        
        