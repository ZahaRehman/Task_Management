from .. import database, Schemas, models
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status, HTTPException
from ..repository import project
from typing import List
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
    return project.create_project(request,db,current_user)
 

@router.get('/',response_model=List[Schemas.ShowProject])
def get_all_Projects(db: Session = Depends(get_db),current_user: Schemas.User=Depends(get_current_user)):
    return project.get_all(db,current_user)

@router.get('/{id}',status_code=200,response_model=Schemas.ShowProject)
def get_Projects_by_id(id, db:Session=Depends(get_db)):
    return project.show(id, db)



@router.put('/{id}')
def get_Projects(id):
    return f"update project with id {id}"


@router.get('/{id}')
def get_Projects(id):
    return f"get project with id {id}"



@router.delete('/{id}')
def get_Projects(id):
    return f"Delete project with id {id}"




