from sqlalchemy.orm import Session
from .. import models, Schemas
from fastapi import HTTPException,status
from ..hashing import Hash

def create_task(project_id: int, request: Schemas.Task, db: Session):
    project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    new_task = models.Task(
        title=request.title,
        description=request.description,
        project_id=project_id
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task