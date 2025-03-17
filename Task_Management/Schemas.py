
from pydantic import BaseModel
from typing import List,Optional


class User(BaseModel):
    name: str
    email: str
    role: str
    password: str

class Project(BaseModel):
    title: str
    description: str


class ProjectResponse(Project):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class ShowProject(BaseModel):
    title: str
    description: str
    class Config():
        orm_mode= True


class Task(BaseModel):
    title: str
    description: str
    assigned_user_id: Optional[int] = None

class TaskCreat(Task):
    project_id: int

class TaskShow(Task):
    
    id: int
    status: str
    assigned_user_id: Optional[int] = None

    class Config:
        orm_mode = True



class ShowUser(BaseModel):
    name: str
    email: str
    role: str
    class Config():
        orm_mode= True

  
class Login(BaseModel):
    username: str
    password: str
  
    
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None