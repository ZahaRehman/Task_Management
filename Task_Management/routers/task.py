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
def create_task(
    id: int, 
    request: Schemas.Task, 
    db: Session = Depends(get_db), 
    current_user: models.User = Depends(get_current_user)
):
        if  current_user.role not in ("admin", "manager"):
            raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have access to Update"
        ) 
        return task.create_task(id, request, db, current_user)

@router.put("/{id}")
def update_task(
    id: int, 
    request: Schemas.Task, 
    db: Session = Depends(get_db), 
    current_user: models.User = Depends(get_current_user)
):
    if  current_user.role not in ("user", "manager"):
            raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have access to Update"
        ) 
    return task.update_task(id, request, db, current_user)