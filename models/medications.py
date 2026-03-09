from sqlalchemy import Integer, String, Boolean, DateTime, Column, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func


Base = declarative_base()

class Medications(Base):
    __tablename__ = "medications"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    is_active = Column(Boolean, default=True)

    batches = relationship("Batches", back_populates="medication")
    prescription = relationship("Prescriptions", back_populates="medication")