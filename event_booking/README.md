## Event Booking - FastAPI Project

This is a FastAPI application for booking event tickets. The project is written in Python and uses industry best practices for API development.

### Project Information

* **Title:** Event Booking
* **Author:** David Nwolu
* **License:** MIT

### Functionality

This API allows users to book tickets for events. Users can provide details about the event, attendee, and desired ticket type. The API processes the booking and returns a confirmation message.

### Installation

1. Clone this repository.
2. Create a virtual environment and activate it.
3. Install the required dependencies:

```bash
pip install fastapi pydantic[email]
```

4. Run the application:

```bash
uvicorn main:app --reload
```

This will start the API server on port 8000 by default.

### Usage

The API exposes an endpoint for booking events:

```
POST /booking/
```

The request body should be a JSON object following the `Event` model defined in `model.py`.

**Example Request:**

```json
{
  "name": "TechSpark Summit",
  "date": "2024-05-10",
  "location": "Royal Albert Hall, London, UK",
  "ticket_types": {
    "ticket_type": "standard"
  },
  "attendee": {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "age": 30
  }
}
```

**Example Response:**

```json
{
  "data": {
    "event_name": "TechSpark Summit",
    "event_date": "2024-05-10",
    "event_location": "Royal Albert Hall, London, UK",
    "attendee_name": "John Doe",
    "attendee_age": 30,
    "attendee_email": "john.doe@example.com",
    "event_ticket_type": "standard"
  },
  "message": "Booking successful"
}
```

### Models

The `model.py` file defines the data models used by the API.

* `Ticket`: Represents a ticket type for an event.
* `Attendee`: Represents an attendee who is booking a ticket.
* `Event`: Represents an event for which tickets can be booked.

### Routes

The `routes.py` file defines the API endpoints. Currently, there is a single endpoint for booking events:

* `/booking/`:  Processes an event booking request.

### Services

The `services.py` file contains business logic for processing event bookings. The `process_booking` function takes an `Event` object as input and returns a confirmation message.

### Testing

The `test_main.py` file contains unit tests for the API functionality. These tests ensure that the API behaves as expected.

The project uses pytest for testing and provides coverage reports using the `cov` library. 

**Test Coverage Report**

The coverage report shows that all lines of code in the project are covered by tests.

**Pytest Report**

The pytest report shows that all tests pass successfully.

### Conclusion

This FastAPI project demonstrates a well-structured and documented API for event booking. The project utilizes industry best practices for API development and includes unit tests for code coverage.

Keep building great APIs! 