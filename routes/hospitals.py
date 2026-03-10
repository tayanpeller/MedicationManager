from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
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

@router.get("", response_model=List[HospitalRead])
def hospital_get(db: Session = Depends(get_db)):
    hospitals = db.query(Hospitals).all()

    return hospitals
 
@router.get("/{hospital_id}", response_model=HospitalRead)
def hospital_get_by_id(hospital_id: int, db: Session = Depends(get_db)):
    hospital = db.query(Hospitals).filter(Hospitals.id == hospital_id).first()

    if not hospital:
        raise HTTPException(
            status_code=404,
            detail="Hospital Not Found"
        )
    
    return hospital