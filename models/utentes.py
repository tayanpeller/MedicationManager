from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.orm import relationship
from users import Users


class Utentes(Users):
    __talbename__ = "users"

    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False)

    doctor = relationship("Doctors", back_populates="utentes")
    prescription = relationship("Prescriptions", back_populates="utente")