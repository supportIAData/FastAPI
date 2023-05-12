from fastapi import FastAPI, Request, Depends
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Union
from app.db.models import Case
from app.db import crud, models, schemas
from app.db.database import SessionLocal, engine
import os

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

script_dir = os.path.dirname(__file__)
static = os.path.join(script_dir, "static/")
templates = os.path.join(script_dir, "templates/")
app.mount("/static", StaticFiles(directory=static), name="static")

templates = Jinja2Templates(directory=templates)

@app.get("/home", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "hello"})

@app.get("/cases", response_class=HTMLResponse)
def read_cases( request :Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db) ):
    cases = crud.get_cases(db, skip=skip, limit=limit)

    return templates.TemplateResponse("cases.html", {"request": request, "cases": cases })

