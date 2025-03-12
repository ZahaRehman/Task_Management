from fastapi import FastAPI ,Depends, status, Response, HTTPException
from .import Schemas
from .import models
from .database import engine, get_db
from .routers import  auth


app = FastAPI()

models.Base.metadata.create_all(engine) 

app.include_router(auth.router)
