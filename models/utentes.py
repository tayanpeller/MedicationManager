from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.orm import relationship
from models.users import Users


class Utentes(Users):
    __tablename__ = "utentes"

    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False)

    doctor = relationship("Doctors", back_populates="utentes")
    prescription = relationship("Prescriptions", back_populates="utente")