from .database import allocation_collection
from .models import VehicleAllocation
from .schemas import AllocationCreate
from datetime import date
from fastapi import HTTPException

async def create_allocation(allocation: AllocationCreate):
    existing_allocation = await allocation_collection.find_one({
        "vehicle_id": allocation.vehicle_id,
        "allocation_date": allocation.allocation_date
    })

    if existing_allocation:
        raise HTTPException(status_code=400, detail="Vehicle is already allocated for this date.")

    driver_id = allocation.vehicle_id  # Assume vehicle_id matches driver_id

    new_allocation = VehicleAllocation(
        employee_id=allocation.employee_id,
        vehicle_id=allocation.vehicle_id,
        driver_id=driver_id,
        allocation_date=allocation.allocation_date
    )
    await allocation_collection.insert_one(new_allocation.dict(by_alias=True))
    return new_allocation

async def update_allocation(id: str, allocation: AllocationCreate):
    existing_allocation = await allocation_collection.find_one({"_id": id})
    
    if not existing_allocation:
        raise HTTPException(status_code=404, detail="Allocation not found.")

    if allocation.allocation_date < date.today():
        raise HTTPException(status_code=400, detail="Cannot update past allocations.")

    await allocation_collection.update_one({"_id": id}, {"$set": allocation.dict()})
    return await allocation_collection.find_one({"_id": id})

async def delete_allocation(id: str):
    allocation = await allocation_collection.find_one({"_id": id})

    if not allocation:
        raise HTTPException(status_code=404, detail="Allocation not found.")
    
    if allocation["allocation_date"] < date.today():
        raise HTTPException(status_code=400, detail="Cannot delete past allocations.")

    await allocation_collection.delete_one({"_id": id})
    return True

async def get_allocation_history(filters: dict = None):
    if not filters:
        filters = {}
    allocations = await allocation_collection.find(filters).to_list(1000)
    return allocations
