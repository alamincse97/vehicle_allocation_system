import motor.motor_asyncio
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_DETAILS = os.getenv("MONGO_DETAILS")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
db = client.vehicle_allocation

allocation_collection = db.get_collection("allocations")
