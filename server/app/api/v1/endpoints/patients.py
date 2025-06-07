from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api import deps
from app.schemas.patient import Patient, PatientCreate, PatientUpdate
from app.crud import patient as patient_crud

router = APIRouter()

@router.get("/", response_model=List[Patient])
def read_patients(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user = Depends(deps.get_current_active_user),
):
    """
    Retrieve patients.
    """
    patients = patient_crud.get_patients(db, skip=skip, limit=limit)
    return patients

@router.post("/", response_model=Patient)
def create_patient(
    *,
    db: Session = Depends(deps.get_db),
    patient_in: PatientCreate,
    current_user = Depends(deps.get_current_active_user),
):
    """
    Create new patient.
    """
    try:
        # Convert the input to dict and validate
        patient_data = patient_in.dict()
        # Create the patient
        patient = patient_crud.create_patient(db=db, patient=patient_in)
        return patient
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.get("/{patient_id}", response_model=Patient)
def read_patient(
    *,
    db: Session = Depends(deps.get_db),
    patient_id: int,
    current_user = Depends(deps.get_current_active_user),
):
    """
    Get patient by ID.
    """
    patient = patient_crud.get_patient(db=db, patient_id=patient_id)
    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patient not found"
        )
    return patient

@router.put("/{patient_id}", response_model=Patient)
def update_patient(
    *,
    db: Session = Depends(deps.get_db),
    patient_id: int,
    patient_in: PatientUpdate,
    current_user = Depends(deps.get_current_active_user),
):
    """
    Update a patient.
    """
    patient = patient_crud.get_patient(db=db, patient_id=patient_id)
    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patient not found"
        )
    patient = patient_crud.update_patient(
        db=db, patient_id=patient_id, patient=patient_in
    )
    return patient

@router.delete("/{patient_id}", response_model=bool)
def delete_patient(
    *,
    db: Session = Depends(deps.get_db),
    patient_id: int,
    current_user = Depends(deps.get_current_active_user),
):
    """
    Delete a patient.
    """
    patient = patient_crud.get_patient(db=db, patient_id=patient_id)
    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patient not found"
        )
    return patient_crud.delete_patient(db=db, patient_id=patient_id) 