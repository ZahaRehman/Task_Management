from fastapi import FastAPI ,Depends, status, Response, HTTPException
from .import Schemas
from .import models
from .database import engine, get_db
from .routers import  auth, project, task, user


app = FastAPI()

models.Base.metadata.create_all(engine) 

app.include_router(auth.router)
app.include_router(project.router)
app.include_router(task.router)
app.include_router(user.router)