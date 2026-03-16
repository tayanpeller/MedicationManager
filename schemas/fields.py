from pydantic import BaseModel
from models.fields import EnumFields
from datetime import datetime
from typing import Optional

class FieldsResponse(BaseModel):
    description: EnumFields
