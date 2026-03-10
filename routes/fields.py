from fastapi import APIRouter, Depends, HTTPException
from models.fields import Fields
from schemas.fields import FieldsPrivate, FieldsResponse
from sqlalchemy.orm import Session
from db.config import get_db
from typing import List

router = APIRouter(prefix="/fields", tags=["fields"])

@router.get("", response_model=List[FieldsResponse])
def get_all_fields(db: Session = Depends(get_db)):
    fields_list = db.query(Fields).filter(Fields.is_active == True).all()

    if not fields_list:
        raise HTTPException(
            status_code=404,
            detail= "No Fields Available!"
        )
    
    return fields_list