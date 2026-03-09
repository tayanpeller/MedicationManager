from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.orm import relationship
from models.users import Users


class Doctors(Users):
    __tablename__ = "doctors"

    field_id = Column(Integer, ForeignKey("fields.id"), nullable=False)
    hospital_id = Column(Integer, ForeignKey("hospitals.id"), nullable=False)
    
    field = relationship("Fields", back_populates="doctor")
    hospital = relationship("Hospitals", back_populates="doctor")
    
    utentes = relationship("Utentes", back_populates="doctor")
    clinicians = relationship("Clinicians", back_populates="doctor")
    prescriptions = relationship("Prescriptions", back_populates="doctor")