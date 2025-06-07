from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, EmailStr

class PatientBase(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: date
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    medical_history: Optional[str] = None

    class Config:
        orm_mode = True

class PatientCreate(PatientBase):
    pass

class PatientUpdate(PatientBase):
    pass

class Patient(PatientBase):
    id: int
    last_visit: datetime
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "first_name": "John",
                "last_name": "Doe",
                "date_of_birth": "1990-01-01",
                "email": "john@example.com",
                "phone": "+1234567890",
                "address": "123 Main St",
                "medical_history": "No known allergies",
                "last_visit": "2024-03-19T00:00:00",
                "created_at": "2024-03-19T00:00:00",
                "updated_at": "2024-03-19T00:00:00"
            }
        } 