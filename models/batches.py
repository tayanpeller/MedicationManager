from sqlalchemy import Integer, String, Boolean, DateTime, Column, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func



Base = declarative_base()

class Batches(Base):
    __tablename__ = "batches"

    id = Column(Integer, primary_key=True)
    validation = Column(DateTime(timezone=True), nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    is_active = Column(Boolean, default=True)

    medication_id = Column(Integer,ForeignKey("medications.id"), nullable=False)
    medication = relationship("Medications", back_populates="batches")