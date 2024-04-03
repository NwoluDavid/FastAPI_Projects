# Flight Booking API

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

#### Author: David Nwolu

The Flight Booking API project provides a FastAPI route for booking flights. It utilizes request body parameters for passenger information (name, age, contact details), flight details (origin, destination, date), and seat preferences. String validation is implemented for passenger names and contact details, while numeric validation is applied for passenger age and flight-related fields. Seat preferences are validated to ensure they are within valid options. The API simulates the flight booking process and returns booking confirmation upon successful booking.

## Technologies Used

- Python 3.7+
- FastAPI
- Pydantic (for data validation)

## Installation

1. Clone this repository:

    ```bash
    git clone <repository_url>
    ```

2. Navigate to the project directory:

    ```bash
    cd flight-booking-api
    ```

3. Install dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the FastAPI server:

    ```bash
    uvicorn main:app --reload
    ```

2. The API will be running locally at `http://localhost:8000`.

3. Use an API client like `curl` or tools like Postman to make requests to the provided endpoints.

## Endpoints

- **POST /book_flight:** Book a flight.
    - Request body parameters:
        - Passenger information: `name`, `age`, `contact_details`.
        - Flight details: `origin`, `destination`, `date`.
        - Seat preferences: `seat_preference`.
    - String validation is applied for passenger names and contact details.
    - Numeric validation is applied for passenger age and flight-related fields.
    - Seat preferences are validated to ensure they are within valid options.
    - Simulates the flight booking process and returns booking confirmation.

## Examples

### Book a flight

```bash
curl -X POST "http://localhost:8000/book_flight" \
     -H "Content-Type: application/json" \
     -d '{
        "name": "John Doe",
        "age": 30,
        "contact_details": "john.doe@example.com",
        "origin": "New York",
        "destination": "Los Angeles",
        "date": "2024-04-15",
        "seat_preference": "Window"
     }'
```

### Example Response (Success)

```json
{
    "message": "Flight booked successfully. Booking confirmation sent to john.doe@example.com"
}
```

## Documentation

Additional documentation or resources related to this project will be available soon.

## Contributing

If you'd like to contribute to this project, feel free to open an issue or submit a pull request. Contributions are always welcome!

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as per the terms of the license.