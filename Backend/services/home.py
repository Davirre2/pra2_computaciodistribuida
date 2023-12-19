#aquí hi ha les consultes a BD i tal
import pytest
from sqlmodel import Session
#from requests import Session quin dels dos es xd

import schemas.home
import database.database as database
import models.home as home
import schemas.home as schemas
from fastapi import FastAPI, Depends
#from sqlmodel import Session, create_engine, select

app = FastAPI()

async def get_home_list(Id: int, payload: schemas.HomeList):
    #engine = create_engine("sqlite:///localhost") #nidea

    db = Depends(database.get_db())
    id = 1
    test_home = {"id": id,"home_name": "My Home", "home_description": "Description", "home_address": "123 Main St","owner": 1, }
    #create_home(test_home, db)
    homes = db.query(home.Home).filter(home.Home.id == id).all()
    print (homes)
    return homes

def test_homee():
    pn = home.Home(id=1, home_name="country", home_description="code", home_address="number", owner="1", rooms="AS")

    assert pn.id == 1
    assert pn.home_name == 'country'
    assert pn.home_description == 'code'
    assert pn.home_address == 'number'
    assert pn.owner == '1'
    return pn

async def get_home_test(db: Session):
    #engine = create_engine("sqlite:///localhost") #nidea
    id = 1
    test_home = test_homee()
    #create_home(test_home, db)
    deb = next(db)
    
    deb.add(test_home)
    deb.commit()
    deb.refresh(test_home)
    #homes = db.query(home.Home).filter(home.Home.id == id).all()
    print ("homes")
    return "homes"


async def post_home(Home: home, db: Session = Depends(database.get_db)):
    await db.add(home) #no sé si calen els await
    await db.commit()
    await db.refresh(home)
    return home

# @app.get("/home/{owner:str}")
# async def get_home_list_by_owner(owner: int):
#     engine = create_engine("sqlite:///localhost") #nidea

#     with Session(engine) as session:
#         statement = select(home).where(home.owner == owner)
#         result = session.exec(statement).first()
#         print(result)
#     return result

# @app.put("/home")
# async def modify_home(User: str):
#     engine = create_engine("sqlite:///localhost") #nidea

#     with Session(engine) as session:
#         statement = select(home)
#         result = session.exec(statement).first()
#         print(result)
#     return result

# @app.post("/home")
# async def create_home(home_name: str, home_address: str, home_description:str, owner:str):
#     engine = create_engine("sqlite:///localhost") #nidea
#     record = home(home_name = home_name, home_address = home_address, home_description = home_description, owner = owner)
#     with Session(engine) as session:
#         session.add(record)
#         session.commit()
#     return print("hola")

# @app.get("/home")
# async def get_home_list():
#     engine = create_engine("sqlite:///localhost") #nidea

#     with Session(engine) as session:
#         statement = select(home)
#         result = session.exec(statement).first()
#         print(result)
#     return result