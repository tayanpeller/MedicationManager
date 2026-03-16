from pydantic import BaseModel

class AdminsSchema(BaseModel):
    firstname: str
    lastname: str
    email: str
    password: str
    is_active: bool
    is_admin: bool