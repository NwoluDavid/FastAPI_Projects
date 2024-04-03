from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_inventory():
    # Test case for retrieving all vehicles
    response = client.get("/vehicles/")
    assert response.status_code == 200
    assert len(response.json()["vehicle"]) == 50  # Assuming 50 vehicles in the database

    # Test case for filtering vehicles by make
    response = client.get("/vehicles/?make=Toyota")
    assert response.status_code == 200
    assert len(response.json()["vehicle"]) == 10  # Assuming there are 6 Toyota vehicles

    # Test case for filtering vehicles by model
    response = client.get("/vehicles/?model=Corolla")
    assert response.status_code == 200
    assert len(response.json()["vehicle"]) == 1  # Assuming only 1 Corolla in the database

    # Test case for filtering vehicles by price range
    response = client.get("/vehicles/?price_range=15000_16000")
    assert response.status_code == 200
    assert len(response.json()["vehicle"]) == 2  # Assuming 2 vehicles within the price range

    # Test case for filtering vehicles by make, model, and price range
    response = client.get("/vehicles/?make=Toyota&model=Corolla&price_range=15000_16000")
    assert response.status_code == 200
    assert len(response.json()["vehicle"]) == 1  # Assuming only 1 matching vehicle

def test_read_inventory_id():
    # Test case for retrieving a vehicle by valid ID
    response = client.get("/vehicles/1")
    assert response.status_code == 200
    assert response.json()["vehicle"]["vehicle_id"] == 1

    # Test case for retrieving a vehicle by invalid ID
    response = client.get("/vehicles/1000")
    assert response.status_code == 200

    # Test case for retrieving a vehicle by non-integer ID
    response = client.get("/vehicles/abc")
    assert response.status_code == 422

