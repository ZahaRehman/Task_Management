from sqlalchemy.orm import Session
from .. import models, Schemas
from fastapi import HTTPException,status
from ..hashing import Hash


def create_project(request: Schemas.Project,db:Session):
    new_project = models.Project(name=request.name, description= request.description)
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project