from pydantic import BaseModel
from models.fields import EnumFields
from datetime import datetime
from typing import Optional

class FieldsResponse(BaseModel):
    description: EnumFields

class Fields(FieldsResponse):
    timeframe: int
    is_active: bool
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True