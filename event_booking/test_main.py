import json
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_booking():
    # Define a sample booking data
    booking_data = {
        "name": "TechSpark Summit",
        "date": "2024-04-02",
        "location": "Royal Albert Hall London, UK",
        "ticket_types": {
            "ticket_type": "standard"
        },
        "attendee": {
            "name": "John Mac",
            "email": "john@example.com",
            "age": 25
        }
    }

    # Send a POST request to the /booking endpoint
    response = client.post("/booking/", json=booking_data)

    # Assert that the response status code is 201 (Created)
    assert response.status_code == 201

    # Parse the JSON response
    response_json = response.json()

    # Assert that the response contains the expected keys
    assert "data" in response_json
    assert "message" in response_json

    # Assert that the booking data in the response matches the submitted data
    assert response_json["data"]["event_name"] == booking_data["name"]
    assert response_json["data"]["event_date"] == booking_data["date"]
    assert response_json["data"]["event_location"] == booking_data["location"]
    assert response_json["data"]["attendee_name"] == booking_data["attendee"]["name"]
    assert response_json["data"]["attendee_age"] == booking_data["attendee"]["age"]
    assert response_json["data"]["attendee_email"] == booking_data["attendee"]["email"]
    assert response_json["data"]["event_ticket_type"] == booking_data["ticket_types"]["ticket_type"]

    # Assert that the message in the response is correct
    assert response_json["message"] == "Booking successful"
