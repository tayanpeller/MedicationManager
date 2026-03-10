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
    hospitals = db.query(Hospitals).filter(Hospitals.is_active == True).all()

    if not hospitals:
        raise HTTPException(
            status_code=404,
            detail="No Hospitals Available"
        )

    return hospitals
 
@router.get("/{hospital_id}", response_model=HospitalRead)
def hospital_get_by_id(hospital_id: int, db: Session = Depends(get_db)):
    hospital = db.query(Hospitals).filter(Hospitals.id == hospital_id, Hospitals.is_active == True).first()

    if not hospital:
        raise HTTPException(
            status_code=404,
            detail="Hospital Not Found"
        )
    
    return hospital

@router.put("/{hospital_id}", response_model=HospitalRead)
def hospital_update_by_id(hospital_id: int, updateHospital: HospitalUpdate, db:  Session = Depends(get_db)):
    hospital = db.query(Hospitals).filter(Hospitals.id == hospital_id).first()

    if not hospital:
        raise HTTPException(
            status_code=404,
            detail=f"Hospital with ID: {hospital_id} Not Found!"
        )
    
    hospital.name = updateHospital.name #type: ignore
    
    db.commit()
    db.refresh(hospital)

    return hospital


@router.delete("/{hospital_id}", response_model=HospitalRead)
def hospitals_delete_by_id(hospital_id:int, db: Session = Depends(get_db)):
    hospital = db.query(Hospitals).filter(Hospitals.id == hospital_id).first()

    if not hospital:
        raise HTTPException(
            status_code=404,
            detail="Hospital not found in DataBase!"
        )
    
    hospital.is_active = False #type: ignore

    db.commit()
    db.refresh(hospital)
    
    return hospital