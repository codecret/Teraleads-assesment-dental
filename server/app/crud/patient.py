from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.patient import Patient
from app.schemas.patient import PatientCreate, PatientUpdate

def get_patient(db: Session, patient_id: int) -> Optional[Patient]:
    return db.query(Patient).filter(Patient.id == patient_id).first()

def get_patient_by_email(db: Session, email: str) -> Optional[Patient]:
    return db.query(Patient).filter(Patient.email == email).first()

def get_patients(
    db: Session, skip: int = 0, limit: int = 100
) -> List[Patient]:
    return db.query(Patient).offset(skip).limit(limit).all()

def create_patient(db: Session, patient: PatientCreate) -> Patient:
    patient_data = patient.dict()
    db_patient = Patient(**patient_data)
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def update_patient(
    db: Session, patient_id: int, patient: PatientUpdate
) -> Optional[Patient]:
    db_patient = get_patient(db, patient_id)
    if db_patient:
        update_data = patient.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_patient, field, value)
        db.commit()
        db.refresh(db_patient)
    return db_patient

def delete_patient(db: Session, patient_id: int) -> bool:
    db_patient = get_patient(db, patient_id)
    if db_patient:
        db.delete(db_patient)
        db.commit()
        return True
    return False 