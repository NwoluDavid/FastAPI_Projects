from fastapi.testclient import TestClient
from main import app
import json

# Create a test client using the TestClient class
client = TestClient(app)

# Test the create_booking route
def test_create_booking():
# Update the key in the test data to match the expected JSON
    response = client.post(
        "/booking/",
        json={
            "seat_pref": "A1",
            "contact_details": {
                "name": "John Doe",
                "age": 25,
                "email": "user@example.com",
                "phone": "+2348123456789",
                "next_of_kin": "Jane Doe",
            },
            "flight_details": {
                "origin": "Lagos",
                "destination": "Abuja",
                "flight_date": "2021-12-25",
            },
        },
    )


    assert response.status_code == 201

    # Serialize both actual and expected JSON responses with sorted keys
    actual_json = json.dumps(response.json(), sort_keys=True)
    expected_json = json.dumps({
        "data": {
            "customer_name": "John Doe",  # Update to match the actual customer name
            "customer_age": 25,
            "customer_email": "user@example.com",  # Update to match the actual customer email
            "customer_phone": "tel:+234-812-345-6789",
            "flight_origin": "Lagos",
            "flight_destination": "Abuja",
            "flight_date": "2021-12-25",
            "seat_preference": "A1"
        },
        "message": "Booking successful"
    }, sort_keys=True)

    # Perform assertion with sorted JSON strings
    assert actual_json == expected_json

