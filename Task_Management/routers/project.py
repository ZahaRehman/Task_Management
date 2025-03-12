from .. import database, Schemas, models
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status, HTTPException
from ..repository import user
from ..hashing import Hash

get_db = database.get_db


router = APIRouter(
    prefix='/project',
    tags=["project"]
)

@router.post('/')
def create_project():
    return "post project"
 
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




