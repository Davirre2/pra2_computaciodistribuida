from exceptions.WrongUserException import WrongUserException
from models.home import Home
import schemas.home as schemas
from models.tokendata import TokenData
from exceptions.EmptyPayloadException import EmptyPayloadException

class HomeService:
    
    def __init__(self, service_session) -> None:
        self.db = service_session

    def get_home_list_by_id(self, Id: int):
        homes = self.db.query(Home).filter(Home.id == Id).first()
        return homes
    
    def get_home_list_by_owner_id(self, Id: int):
        homes = self.db.query(Home).filter(Home.owner_id == Id).all()
        return homes
    
    def get_home_list(self):
        homes = self.db.query(Home).all()
        return homes
    
    def create_home(self, created_home: schemas.HomeCreate):
        new_home = Home(**created_home.dict())
        self.db.add(new_home)
        self.db.commit()
        self.db.refresh(new_home)
        return new_home
    
    def delete_home(self, id: int, data: TokenData):
        home = self.db.query(Home).filter(Home.id == id).first()
        if not home.owner_id == data.user_id:
            raise WrongUserException("L'usuari no és el propietari de la casa")
        self.db.delete(home)
        self.db.commit()
        return home
    
    def update_home(self, id: int, new_name: str, new_address: str, new_description: str, data: TokenData):
        home = self.db.query(Home).filter(Home.id == id).first()
        if not home.owner_id == data.user_id:
            raise WrongUserException("L'usuari no és el propietari de la casa")
        
        if home.home_name is not  new_name and new_name is not None:
            self.db.query(Home).filter(Home.id == id).update({Home.home_name: new_name}, synchronize_session = False)
        if home.home_address is not  new_address and new_address is not None:
            self.db.query(Home).filter(Home.id == id).update({Home.home_address: new_address}, synchronize_session = False)
        if home.home_description is not  new_description and new_description is not None:
            self.db.query(Home).filter(Home.id == id).update({Home.home_description: new_description}, synchronize_session = False)
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
        
        return list_homes
        
        