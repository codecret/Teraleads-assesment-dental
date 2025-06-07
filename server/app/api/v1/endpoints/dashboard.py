from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta
from app.db.session import get_db
from app.models.patient import Patient
from app.core.security import get_current_user

router = APIRouter()

@router.get("/stats")
def get_dashboard_stats(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """
    Get dashboard statistics including total patients, new patients this month,
    and appointments for today.
    """
    # Get total patients
    total_patients = db.query(func.count(Patient.id)).scalar()

    # Get new patients this month
    first_day_of_month = datetime.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    new_patients_this_month = db.query(func.count(Patient.id))\
        .filter(Patient.created_at >= first_day_of_month)\
        .scalar()

    # For now, we'll return 0 for appointments as we haven't implemented that yet
    appointments_today = 0

    return {
        "totalPatients": total_patients,
        "newPatientsThisMonth": new_patients_this_month,
        "appointmentsToday": appointments_today
    } 