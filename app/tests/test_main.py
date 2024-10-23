from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Vehicle Allocation System"}

def test_allocate_vehicle():
    response = client.post("/allocations/", json={
        "employee_id": 1,
        "vehicle_id": 1,
        "allocation_date": "2024-10-25"
    })
    assert response.status_code == 200

def test_allocation_history():
    response = client.get("/allocations/")
    assert response.status_code == 200
