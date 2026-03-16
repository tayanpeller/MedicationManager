from sqlalchemy import Column, Boolean
from models.users import Users

class Admins(Users):
    __tablename__ = "admins"

    is_admin = Column(Boolean, default=True)

    def __init__(self, firstname, lastname, email, hash_pwd, is_active=True, is_admin=True):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.hash_pwd = hash_pwd
        self.is_active = is_active
        self.is_admin = is_admin