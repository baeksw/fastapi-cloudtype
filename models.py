from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Table

from sqlalchemy import Column, Integer, String, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base

from database import Base

class TwCafe(Base):
    __tablename__ = 'TW_CAFE'
    __table_args__ = {"autoload": True, 'extend_existing': True } 

    id = Column(Integer, primary_key=True, autoincrement=True )   
