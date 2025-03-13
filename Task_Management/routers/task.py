from .. import database, Schemas, models
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status, HTTPException
from ..repository import user
from ..hashing import Hash
from ..oauth2 import get_current_user
from ..repository import task
get_db = database.get_db


router = APIRouter(
    prefix='/task',
    tags=["Tasks"]
)


@router.post("/projects/{id}/tasks", status_code=status.HTTP_201_CREATED)
def create_task(id: int, request: Schemas.Task, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return "test" 

