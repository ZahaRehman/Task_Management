from sqlalchemy.orm import Session
from .. import models, Schemas
from fastapi import HTTPException,status
from ..hashing import Hash

def create_project(request: Schemas.Project, db: Session, current_user: models.User):
    if current_user.role.lower() not in ["admin", "manager"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only Admins or Managers can create projects."
        )
    
    new_project = models.Project(
        title=request.title,
        description=request.description,
        owner_id=current_user.id 
    )
    
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project