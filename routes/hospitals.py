from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models.hospitals import Hospitals
from schemas.hospitals import *
from db.config import get_db

router = APIRouter(prefix="/hospitals", tags=["hospitals"])

@router.post("", response_model=HospitalRead)
def hospital_create(hospital: HospitalCreate, db: Session = Depends(get_db)):
    new_hospital = Hospitals(name=hospital.name)

    db.add(new_hospital)
    db.commit()
    db.refresh(new_hospital)

    return new_hospital