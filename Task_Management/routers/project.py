from .. import database, Schemas, models
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status, HTTPException
from ..repository import project
from ..hashing import Hash
from ..database import get_db 
from ..oauth2 import get_current_user

get_db = database.get_db


router = APIRouter(
    prefix='/project',
    tags=["project"]
)

@router.post('/')
def create_project(request : Schemas.Project, db: Session = Depends(get_db) ,current_user: Schemas.User=Depends(get_current_user)):
    return project.create_project(request,db)
 

@router.get('/')
def get_Projects():
    return "get all project"

@router.get('/{id}')
def get_Projects(id):
    return f"get project with id {id}"



@router.put('/{id}')
def get_Projects(id):
    return f"update project with id {id}"


@router.get('/{id}')
def get_Projects(id):
    return f"get project with id {id}"



@router.delete('/{id}')
def get_Projects(id):
    return f"Delete project with id {id}"




