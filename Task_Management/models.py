from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    role = Column(String)
    password = Column(String)
 
 
class Project(Base):
    __tablename__ = 'Project'
    
    id = Column(Integer, primary_key=True, index=True) 
    name = Column(String)
    description =Column(String)