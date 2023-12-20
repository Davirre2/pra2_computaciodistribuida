from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = ""
engine = None
SessionLocal = None

SQLALCHEMY_DATABASE_URL = "sqlite:///./database/sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args = {"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

from models.user import User
from models.home import Home
#import models.home
from models.room import Room


Base.metadata.create_all(bind=engine)

def get_all_db_data():
    return(SQLALCHEMY_DATABASE_URL, engine, SessionLocal, Base)

def db_get(): 
    return SessionLocal()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()
    finally:
        db.close()