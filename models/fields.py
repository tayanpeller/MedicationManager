from sqlalchemy import Integer, Float, Boolean, String, DateTime, ForeignKey, Column, Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base, relationship
import enum

Base = declarative_base()


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

    doc_relation = relationship("Doctors", back_populates="field_relation")