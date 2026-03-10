from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.users import Users


class Clinicians(Users):
    __tablename__ = "clinicians"

    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False)
    doctor = relationship("Doctors", back_populates="clinicians")

    hospital_id = Column(Integer, ForeignKey("hospitals.id"), nullable=False)
    hospital = relationship("Hospitals", back_populates="clinicians")

    prescriptions = relationship("Prescriptions", back_populates="clinician")