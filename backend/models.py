from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String)
    owner = Column(String)

    # Establish relationship with metrics
    metrics = relationship("Metric", back_populates="project")

class Metric(Base):
    __tablename__ = "metrics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    value = Column(Float)
    project_id = Column(Integer, ForeignKey("projects.id"))

    # Link back to the project
    project = relationship("Project", back_populates="metrics")
