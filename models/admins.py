from sqlalchemy import Column, Boolean
from users import Users

class Admins(Users):
    __tablename__ = "admins"

    is_admin = Column(Boolean, default=True)