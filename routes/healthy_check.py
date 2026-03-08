from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from db.config import get_db

router = APIRouter()

@router.get("/healthy_check")
async def healthy_check(db: Session=Depends(get_db)):
    try:
        result = db.execute(text("SELECT 1")).scalar()
        db_status = {"STATUS": "healthy", "DB_CHECK": result}

    except Exception as e:
        db_status = {"STATUS": "unhealthy", "DB_CHECK": str(e)}

    return db_status