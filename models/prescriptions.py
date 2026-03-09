from sqlalchemy import Integer, Boolean, DateTime, Float, Column, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class Prescriptions(Base):
    __tablename__ = "prescriptions"

    id = Column(Integer, primary_key=True)

    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False)
    clinician_id = Column(Integer, ForeignKey("clinicians.id"), nullable=True)
    utente_id = Column(Integer, ForeignKey("utentes.id"), nullable=False)
    medication_id = Column(Integer, ForeignKey("medications.id"), nullable=False)

    dosage = Column(Float, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    is_active = Column(Boolean, default=True)

    doctor = relationship("Doctors", back_populates="prescriptions")
    clinician = relationship("Clinicians", back_populates="prescriptions")
    utente = relationship("Utentes", back_populates="prescriptions")
    medication = relationship("Medications", back_populates="prescriptions")