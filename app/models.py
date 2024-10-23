from pydantic import BaseModel, Field
from datetime import date
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid object id")
        return ObjectId(v)

class VehicleAllocation(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    employee_id: int
    vehicle_id: int
    driver_id: int
    allocation_date: date

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
