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

def get_all(db:Session,current_user: models.User):
    if current_user.role.lower() != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only Admins or Managers can create projects."
        )
    projects= db.query(models.Project).all()
    return projects


def show(id:int,db:Session):
    project= db.query(models.Project).filter(models.Project.id==id).first()
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"project with the id {id} is not available")
        
    return project


def update_project(id: int, request: Schemas.Project, db: Session):
    update_data = request.dict(exclude_unset=True)
    project= db.query(models.Project).filter(models.Project.id == id)
    project_obj = project.first()
    
    if not project_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project with id {id} not found"
        )
    
    project.update(update_data)
    db.commit()
    db.refresh(project_obj)
    return project_obj

def delete_project(id:int, db:Session):
    project= db.query(models.Project).filter(models.Project.id==id)
    project_obj = project.first()
    if not project_obj:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Project with id {id} not found")
    project.delete(synchronize_session=False)
    db.commit()
    return 'done'


