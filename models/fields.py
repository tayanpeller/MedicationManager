from sqlalchemy import Integer, Boolean, DateTime, Column, Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import enum

from models.users import Base


class EnumFields(str, enum.Enum):
    FAMILY = "family medicine"
    PEDIA = "pediatry"
    DERMA = "dermatology"
    PSYCO = "psycology"
    ENDO = "endocrinology"

class Fields(Base):
    __tablename__ = "fields"

    id = Column(Integer, primary_key=True)
    description = Column(Enum(EnumFields), nullable=False)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    timeframe = Column(Integer, nullable=False)
    
    is_active = Column(Boolean, default=True)

    doctors = relationship("Doctors", back_populates="field")