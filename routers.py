from fastapi import FastAPI
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from pydantic import BaseModel
from sqlalchemy import Column, String, Float, Integer
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import schemas, models
from database import SessionLocal


def get_db():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    finally:
        session.close()
TW_CAFE_router = SQLAlchemyCRUDRouter(
    schema=schemas.TwCafeVO,
    create_schema=schemas.TwCafeCreate,
    db_model=models.TwCafe,
    db=get_db,
    prefix='tw_cafe',
    get_all_route=True,
    get_one_route=True,
    delete_all_route=False,
    delete_one_route=False,
    create_route=False,
    update_route=True,
    paginate=25
    )

   


"""

https://fastapi-crudrouter.awtkns.com/routingapp.include_router(routers.TW_CAFE_router)
   



"""
