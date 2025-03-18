from .. import database, Schemas, models, oauth2
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status, HTTPException
from ..repository import user
from ..hashing import Hash
from ..oauth2 import get_current_user
from ..repository import task
get_db = database.get_db
from typing import List


router = APIRouter(
    prefix='/task',
    tags=["Tasks"]
)
@router.post("/projects/{id}/tasks", status_code=status.HTTP_201_CREATED)
def create_task(
    id: int, 
    request: Schemas.Task, 
    db: Session = Depends(get_db), 
    current_user: models.User = Depends(oauth2.get_current_user)
):
        if  current_user.role not in ("admin", "Manager"):
            raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have access to Update"
        ) 
        return task.create_task(id, request, db, current_user)

@router.delete('/{id}', status_code= status.HTTP_204_NO_CONTENT)
def delete_Task(id:int, db: Session = Depends(database.get_db), get_current_user: Schemas.User= Depends(oauth2.get_current_user)):
    if get_current_user.role not in ("user", "Manager"):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have access to Delete"
        )
    return task.delete_task(id,db)


@router.get('/',response_model=List[Schemas.TaskShow])
def get_all_Tasks(db: Session = Depends(get_db)):
    return task.get_all(db)


@router.put("/{id}")
def update_task(
    id: int, 
    request: Schemas.Task, 
    db: Session = Depends(get_db), 
    current_user: models.User = Depends(get_current_user)
):
    if  current_user.role not in ("User", "Manager"):
            raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have access to Update"
        ) 
    return task.update_task(id, request, db, current_user)
