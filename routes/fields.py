from fastapi import APIRouter, Depends, HTTPException
from models.fields import Fields
from schemas.fields import FieldsResponse
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


@router.post("", response_model=FieldsResponse)
def create_field(field: FieldsResponse, db: Session = Depends(get_db)):
    new_field = Fields(description=field.description)

    if not new_field:
        raise HTTPException(
            status_code=404,
            detail="Not a Valid Field"
        )
    
    db.add(new_field)
    db.commit()
    db.refresh(new_field)

    return new_field

@router.get("/{field_id}", response_model=FieldsResponse)
def get_field_by_id(field_id: int, db: Session = Depends(get_db)):
    field = db.query(Fields).filter(Fields.id == field_id, Fields.is_active == True).first()

    if not field:
        raise HTTPException(
            status_code=404,
            detail="Field Not in DataBase!"
        )
    
    return field