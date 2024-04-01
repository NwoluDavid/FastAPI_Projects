# Vehicle Inventory API

The Vehicle Inventory API project provides a FastAPI endpoint for managing vehicle inventory. It utilizes path parameters for vehicle ID and query parameters for filtering by make, model, and price range. Numeric validation is applied for vehicle ID and price range, while string validation is implemented for make and model parameters. The API returns details of a specific vehicle identified by ID or a list of vehicles based on the query parameters. Comprehensive testing with various combinations of parameters ensures the robustness of the API.

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
    cd vehicle-inventory-api
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

- **GET /vehicles/{vehicle_id}:** Retrieve details of a specific vehicle by ID.
    - Path parameter: `vehicle_id` (numeric).
    - Returns details of the vehicle identified by the given ID.

- **GET /vehicles:** Retrieve a list of vehicles based on query parameters.
    - Query parameters: `make`, `model`, `min_price`, `max_price`.
    - Returns a list of vehicles filtered by the specified criteria.

## Examples

### Retrieve details of a specific vehicle

```bash
curl -X GET "http://localhost:8000/vehicles/123"
```

### Example Response

```json
{
    "id": 123,
    "make": "Toyota",
    "model": "Camry",
    "year": 2020,
    "price": 25000.00
}
```

### Retrieve a list of vehicles by make and price range

```bash
curl -X GET "http://localhost:8000/vehicles?make=Toyota&min_price=20000&max_price=30000"
```

### Example Response

```json
[
    {
        "id": 123,
        "make": "Toyota",
        "model": "Camry",
        "year": 2020,
        "price": 25000.00
    },
    {
        "id": 456,
        "make": "Toyota",
        "model": "Corolla",
        "year": 2019,
        "price": 22000.00
    }
]
```

## Documentation

Additional documentation or resources related to this project will be available soon.

## Contributing

If you'd like to contribute to this project, feel free to open an issue or submit a pull request. Contributions are always welcome!

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as per the terms of the license.