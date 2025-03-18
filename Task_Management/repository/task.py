from sqlalchemy.orm import Session
from .. import models, Schemas, oauth2
from fastapi import HTTPException,status, Depends
from ..hashing import Hash


def create_task(project_id: int, request: Schemas.Task, db: Session, current_user: Schemas.User):
    project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    new_task = models.Task(
        title=request.title,
        description=request.description,
        project_id=project_id,
        assigned_user_id = request.assigned_user_id
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


def update_task(project_id: int, request: Schemas, db: Session,current_user:Schemas.User):
    updated_task= db.query(models.Task).filter(models.Task.id==project_id).first()
    
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    updated_task.title= request.title
    updated_task.description = request.description
    db.add(updated_task)
    db.commit()
    db.refresh(updated_task)
    return updated_task

    
def delete_task(id:int, db:Session):
    task= db.query(models.Task).filter(models.Task.id==id)
    task_obj = task.first()
    if not task_obj:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Project with id {id} not found")
    task.delete(synchronize_session=False)
    db.commit()
    return 'done'

def get_all(db:Session):
    tasks= db.query(models.Task).all()
    return tasks
