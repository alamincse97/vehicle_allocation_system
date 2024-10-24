# vehicle_allocation_system

This is a simple CRUD (Create, Read, Update, Delete) application for managing vehicle_allocation_system for employees in a company, built using FastAPI and MongoDB.

## Features

- Create a new vehicle allocation for an employee
- Get all vehicle allocations
- Get a specific vehicle allocation by ID
- Update an existing vehicle allocation (before the allocation date)
- Delete a vehicle allocation (before the allocation date)
- Generate a history report of vehicle allocations with filters (e.g., by employee, vehicle, date range)

## Prerequisites

- Python 3.7+
- FastAPI
- Uvicorn (for running the application)
- MongoDB (for data storage)

## Installation

1. Clone the repository:
   ```
   https://github.com/alamincse97/vehicle_allocation_system.git
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   uvicorn app.main:app --reload

   ```

2. Open your browser and go to `http://localhost:8000/docs` to see the Swagger UI documentation and test the API endpoints.

## API Endpoints

- `POST /allocations/:`: Create a new vehicle allocation
- `GET /allocations/`: Get all vehicle allocations, with optional filters (by employee, vehicle, date range)
- `GET /allocations/{id}`:  Get a specific vehicle allocation by ID
- `PUT /allocations/{id}`: Update an existing vehicle allocation (allowed only before the allocation date)
- `DELETE /allocations/{id}`: Delete a vehicle allocation (allowed only before the allocation date)

## Project Structure

- `app/main.py`:  Contains the FastAPI application and route handlers
- `app/models.py`: Defines the vehicle allocation model using Pydantic

