# Payment Processing API

The Payment Processing API project implements a FastAPI route for processing payments. It utilizes request body parameters including payment amount, card number, expiration date, and CVV. Numeric validation is applied for payment amount and card-related fields, while expiration date format is validated to ensure it's not expired. The route simulates payment processing logic, including validation and authentication. The API is tested with both valid and invalid payment data.

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
    cd payment-processing-api
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

- **POST /process_payment:** Process a payment.
    - Request body should include `amount`, `card_number`, `expiration_date`, and `cvv`.
    - Numeric validation is applied for payment amount and card-related fields.
    - Expiration date format is validated to ensure it's not expired.
    - Simulates payment processing logic including validation and authentication.
    - Returns appropriate response based on payment success or failure.

## Examples

### Process a valid payment

```bash
curl -X POST "http://localhost:8000/process_payment" \
     -H "Content-Type: application/json" \
     -d '{
        "amount": 100,
        "card_number": "1234567812345678",
        "expiration_date": "04/26",
        "cvv": "123"
     }'
```

### Example Response (Success)

```json
{
    "message": "Payment processed successfully"
}
```

### Process an invalid payment (expired card)

```bash
curl -X POST "http://localhost:8000/process_payment" \
     -H "Content-Type: application/json" \
     -d '{
        "amount": 100,
        "card_number": "1234567812345678",
        "expiration_date": "04/20",
        "cvv": "123"
     }'
```

### Example Response (Error - Expired Card)

```json
{
    "detail": "Card is expired"
}
```

## Documentation

Additional documentation or resources related to this project will be available soon.

## Contributing

If you'd like to contribute to this project, feel free to open an issue or submit a pull request. Contributions are always welcome!

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as per the terms of the license.