from sqlalchemy import Integer, Boolean, String, DateTime, Column
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base, relationship
import enum

from models.users import Base


class Hospitals(Base):
    __tablename__ = "hospitals"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    is_active = Column(Boolean, default=True)

    doctors= relationship("Doctors", back_populates="hospital")
    clinicians = relationship("Clinicians", back_populates="hospital")