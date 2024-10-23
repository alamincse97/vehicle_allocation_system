from pydantic import BaseModel
from datetime import date

class AllocationCreate(BaseModel):
    employee_id: int
    vehicle_id: int
    allocation_date: date

class AllocationResponse(AllocationCreate):
    driver_id: int
