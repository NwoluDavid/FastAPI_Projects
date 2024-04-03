# User Registration API

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

#### Author: David Nwolu

This project aims to provide a FastAPI route for user registration, allowing users to register with a username, email, and password. It implements string validation for username and email fields and ensures the password meets certain complexity requirements. Proper error messages are returned for invalid inputs. Additionally, the registration process is simulated using FastAPI TestClient.

## Technologies Used

- Python 3.7+
- FastAPI
- Pydantic (for data validation)
- FastAPI TestClient

## Installation

1. Clone this repository:

    ```bash
    git clone <repository_url>
    ```

2. Navigate to the project directory:

    ```bash
    cd user-registration-api
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

- **POST /register:** Register a new user.
    - Request body should include `username`, `email`, and `password`.
    - Username and email are validated for string format.
    - Password must meet complexity requirements.
    - Returns appropriate error messages for invalid inputs.

## Examples

### Register a new user

```bash
curl -X POST "http://localhost:8000/register" \
     -H "Content-Type: application/json" \
     -d '{
        "username": "user123",
        "email": "user123@example.com",
        "password": "StrongPassword123!"
     }'
```

### Example Response (Success)

```json
{
    "message": "User registered successfully"
}
```

### Example Response (Error - Invalid Email)

```json
{
    "detail": [
        {
            "loc": [
                "body",
                "email"
            ],
            "msg": "invalid email format",
            "type": "value_error"
        }
    ]
}
```

## Documentation

Additional documentation or resources related to this project will be available soon.

## Contributing

If you'd like to contribute to this project, feel free to open an issue or submit a pull request. Contributions are always welcome!

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as per the terms of the license.