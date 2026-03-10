from pydantic import BaseModel

class HospitalCreate(BaseModel):
    name: str


class HospitalUpdate(BaseModel):
    name: str | None = None


class HospitalRead(BaseModel):
    id: int
    name: str
    is_active: bool

    class Config:
        from_attributes = True