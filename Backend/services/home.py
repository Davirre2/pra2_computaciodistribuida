#aquí hi ha les consultes a BD i tal
import Backend.schemas.home

import Backend.models.home as home
import Backend.schemas.home as schemas
from fastapi import FastAPI
from sqlmodel import Session, create_engine, select

app = FastAPI()

async def get_home_list(Id: int, payload: schemas.HomeList):
    engine = create_engine("sqlite:///localhost") #nidea

    with Session(engine) as session:
        statement = select(home).where(home.Id == Id)
        result = session.exec(statement).first()
        print(result)

    return print("holw")

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