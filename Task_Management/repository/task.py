from sqlalchemy.orm import Session
from .. import models, Schemas
from fastapi import HTTPException,status
from ..hashing import Hash

def create_task(request: Schemas.TaskCreate, db: Session, current_user: models.User):
    project = db.query(models.Project).filter(models.Project.id == request.project_id).first()
    
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    new_task = models.Task(
        title=request.title,
        description=request.description,
        project_id=request.project_id
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task