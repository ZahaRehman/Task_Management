from .. import database, Schemas, models
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status, HTTPException
from ..repository import user
from ..hashing import Hash

get_db = database.get_db


router = APIRouter(
    prefix='/task',
    tags=["Tasks"]
)


@router.get('/{id}')
def get_task(id):
    return f"get tasks by id -->{id}"



