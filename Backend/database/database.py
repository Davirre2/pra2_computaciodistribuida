from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = ""
engine = None
SessionLocal = None
Base = declarative_base()


def init_database():
    global SQLALCHEMY_DATABASE_URL, engine, SessionLocal
    #SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db" #TODO canviar esta url
    SQLALCHEMY_DATABASE_URL = "sqlite:///sql_app.db"
    # SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
    #jwt

    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args = {"check_same_thread": False}
    )
    print(engine)    
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    #print("Tot creat-ish?")

def get_all_db_data():
    return(SQLALCHEMY_DATABASE_URL, engine, SessionLocal, Base)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()