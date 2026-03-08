from sqlalchemy import Integer, Float, String, Boolean, DateTime, Column, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Users(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    email = Column(String, nullable=False)
    hash_pwd = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)