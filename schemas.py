from typing import List

from pydantic.main import BaseModel

class OrmBase(BaseModel):
    class Config:
        orm_mode = True

class TwCafeCreate(OrmBase):
    cafe_name : str
    location : str = None
    tables : str = None
    snack : str = None
    toilet : str = None
    cafe_size : str = None
    power_socket : str = None
    address : str = None
    phone : str = None
    ice_coffee : float = None
    latitude : float = None
    longitude : float = None

class TwCafeVO(TwCafeCreate):
    id : int


    
        
