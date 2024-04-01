from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_register_user():
    # Test valid user registration
    valid_user_data = {
        "username": "JohnDoe",
        "email": "johndoe@example.com",
        "password": "StrongPassword123@"
    }
    response = client.post("/register", json=valid_user_data)
    assert response.status_code == 200

    # Test invalid password
    invalid_password_data = {
        "username": "JaneDoe",
        "email": "janedoe@example.com",
        "password": "weak"
    }
    response = client.post("/register", json=invalid_password_data)
    assert response.status_code == 422  # Expecting Unprocessable Entity status code

    # Test invalid email
    invalid_email_data = {
        "username": "AliceDoe",
        "email": "invalid_email",
        "password": "StrongPassword123!"
    }
    response = client.post("/register", json=invalid_email_data)
    assert response.status_code == 422


