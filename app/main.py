from fastapi import FastAPI, HTTPException
from .crud import create_allocation, update_allocation, delete_allocation, get_allocation_history, date
from .schemas import AllocationCreate, AllocationResponse
from typing import List

app = FastAPI()

@app.post("/allocations/", response_model=AllocationResponse)
async def allocate_vehicle(allocation: AllocationCreate):
    return await create_allocation(allocation)

@app.put("/allocations/{id}", response_model=AllocationResponse)
async def update_vehicle_allocation(id: str, allocation: AllocationCreate):
    return await update_allocation(id, allocation)

@app.delete("/allocations/{id}", response_model=bool)
async def delete_vehicle_allocation(id: str):
    return await delete_allocation(id)

@app.get("/allocations/", response_model=List[AllocationResponse])
async def allocation_history(employee_id: int = None, vehicle_id: int = None, date_from: date = None, date_to: date = None):
    filters = {}
    if employee_id:
        filters["employee_id"] = employee_id
    if vehicle_id:
        filters["vehicle_id"] = vehicle_id
    if date_from and date_to:
        filters["allocation_date"] = {"$gte": date_from, "$lte": date_to}

    return await get_allocation_history(filters)

@app.get("/")
async def root():
    return {"message": "Vehicle Allocation System"}
