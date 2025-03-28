from sqlalchemy import Column, Integer, String, ForeignKey, Text
from .database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    role = Column(String)
    password = Column(String)
    
    projects = relationship("Project", back_populates="owner")
 
 
 
class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    tasks= relationship('Task', back_populates="project")
    
    invitations = relationship("Invitation", back_populates="project", cascade="all, delete-orphan")
    owner = relationship("User", back_populates="projects")
    
    
class Task(Base):
    __tablename__ = 'tasks'
   
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    status = Column(String, default="pending") 
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    assigned_user_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    project = relationship("Project", back_populates="tasks")
    assigned_user = relationship("User")
    
    
class Invitation(Base):
    __tablename__ = 'invitations'
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    invited_email = Column(String, nullable=False)
    token = Column(String, unique=True, nullable=False)
    status = Column(String, default="pending")  # e.g., pending, accepted, declined

    project = relationship("Project", back_populates="invitations")