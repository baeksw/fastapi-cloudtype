import os 
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

class Environ:
    
    API_DB_HOST = os.environ.get('API_DB_HOST')
    API_DB_USER = os.environ.get('API_DB_USER')
    API_DB_PW = os.environ.get('API_DB_PW')
    API_DB_NAME = os.environ.get('API_DB_NAME')
    API_DB_PORT = int(os.environ.get('API_DB_PORT'))

    TARGET= os.environ.get('TARGET')
    TARGET_DATABASE= os.environ.get('TARGET_DATABASE')
    
CONN_DB = "api"
CONN_DBNAME = "apidb"

print(f"CONN_DB => {CONN_DB}")
print(f"CONN_DBNAME => {CONN_DBNAME}")

# connect_args={"check_same_thread": False}

class EngineFactory:
    
    @staticmethod
    def get_db_url_with_port(user, password, host , dbname, port):
        return f"mysql+pymysql://{user}:{password}@{host}:{port}/{dbname}"

    @staticmethod
    def get_db_url(user, password, host , dbname):
        return f"mysql+pymysql://{user}:{password}@{host}/{dbname}"

    @classmethod
    def create_engine_API_by(cls, dbname, echo=False, connect_args={}):
        dburl = cls.get_db_url_with_port(
            Environ.API_DB_USER
            , Environ.API_DB_PW
            , Environ.API_DB_HOST
            , dbname
            , Environ.API_DB_PORT
        )
        engine = create_engine(dburl,echo=echo,  connect_args=connect_args)
        return engine 


engine = EngineFactory.create_engine_API_by(CONN_DBNAME, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base(bind=engine)
Base.metadata.reflect(schema=f"{CONN_DBNAME}")
