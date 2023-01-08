import json 
from pathlib import Path 
from typing import List, Union

from fastapi import Depends, FastAPI, HTTPException, Request, Form, APIRouter
from fastapi import FastAPI, Response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse, PlainTextResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

#from farma.toworkable.api import crud, schemas
#from farma.toworkable.api import routers
#from farma.toworkable.api.database import SessionLocal

import crud, schemas
import routers
from database import SessionLocal


app = FastAPI()

BASE_DIR = Path(__file__).parent  
STATIC = BASE_DIR / 'static'
GENERATED = BASE_DIR / 'static' / 'generated'
TEMPLATES = BASE_DIR / 'templates'
TRANS = BASE_DIR / 'trans'

app.mount("/static", StaticFiles(directory=STATIC), name="static")
templates = Jinja2Templates(directory=TEMPLATES)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
app.include_router(routers.TW_CAFE_router)



