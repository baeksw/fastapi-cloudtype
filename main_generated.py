import json 
from typing import List, Union

from fastapi import Depends, FastAPI, HTTPException
from fastapi import FastAPI, Response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from farma.toworkable.api import crud, schemas
from farma.toworkable.api.database import SessionLocal
from farma.toworkable.api import routers

app = FastAPI()

# app.mount("/static", StaticFiles(directory="static"), name="static")
# templates = Jinja2Templates(directory="templates")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
"""
@app.get('/opers/games/{b4_code}', response_model=schemas.OperGamesMasterVO)
def get_game_code(b4_code : str, db : Session = Depends(get_db)):
#     game = crud.get_game_code(db, b4_code)
    game = crud.select_oper_game_master(b4_code, db)
    if game is None:
        raise HTTPException(status_code=404, detail="User not found")
    return game

"""