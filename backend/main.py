from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import List

from .database import engine, SessionLocal
from .models import Base, Project as DBProject, Metric as DBMetric

# Initialize FastAPI app
app = FastAPI()

# Create the tables
Base.metadata.create_all(bind=engine)

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic models for request data validation
class Metric(BaseModel):
    name: str
    value: float

class ProjectCreate(BaseModel):
    name: str
    type: str
    owner: str
    metrics: List[Metric] = []

# Root endpoint to verify the server is running
@app.get("/")
def read_root():
    return {"message": "Welcome to the Metrics API"}

# Endpoint to get all projects
@app.get("/projects")
def get_projects(db: Session = Depends(get_db)):
    projects = db.query(DBProject).all()
    return projects

# Endpoint to create a new project
@app.post("/projects")
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    # Create a new Project instance
    db_project = DBProject(name=project.name, type=project.type, owner=project.owner)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    
    # Add metrics if provided
    for metric in project.metrics:
        db_metric = DBMetric(name=metric.name, value=metric.value, project_id=db_project.id)
        db.add(db_metric)
    db.commit()
    
    return db_project

# Endpoint to add a metric to a specific project
@app.post("/projects/{project_id}/metrics")
def add_metric(project_id: int, metric: Metric, db: Session = Depends(get_db)):
    db_project = db.query(DBProject).filter(DBProject.id == project_id).first()
    if not db_project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    db_metric = DBMetric(name=metric.name, value=metric.value, project_id=project_id)
    db.add(db_metric)
    db.commit()
    db.refresh(db_metric)
    
    return {"message": "Metric added", "metric": db_metric}
