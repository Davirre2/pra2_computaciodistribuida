#aquí hi ha les consultes a BD i tal
import schemas.home
import database.database as database
import models.home as home
import schemas.home as schemas
from fastapi import FastAPI
#from sqlmodel import Session, create_engine, select

app = FastAPI()

async def get_home_list(Id: int, payload: schemas.HomeList):
    engine = create_engine("sqlite:///localhost") #nidea

    db = Depends(database.get_db())
    home_data = {"home_name": "My Home", "home_description": "Description", "home_address": "123 Main St","owner": 1, }
    create_home(test_home, db)
    homes = db.query(Home).filter(models.Home.id == home_id).all()
    print (homes)
    return homes


async def create_home(Home: home, db: Session = Depends(get_db)):
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