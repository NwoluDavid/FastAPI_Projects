# Vehicle Inventory API

The Vehicle Inventory API project provides a FastAPI endpoint for managing vehicle inventory. It utilizes path parameters for vehicle ID and query parameters for filtering by make, model, and price range. Numeric validation is applied for vehicle ID and price range, while string validation is implemented for make and model parameters. The API returns details of a specific vehicle identified by ID or a list of vehicles based on the query parameters. Comprehensive testing with various combinations of parameters ensures the robustness of the API.

## Technologies Used

- Python 3.7+
- FastAPI
- Pydantic (for data validation)

## Installation

1. Clone this repository:

    ```bash
    git clone <https://github.com/NwoluDavid/FastAPI_Projects/tree/staging/Vehicle_inventory>
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

## TEST REPORTS

### Pytest 

"""
        ❯ pytest
    ============= test session starts ==============
    platform linux -- Python 3.12.1, pytest-8.1.1, pluggy-1.4.0
    rootdir: /home/david/FastAPI_Projects
    configfile: pyproject.toml
    plugins: cov-5.0.0, anyio-4.3.0
    collected 2 items                              

    test_main.py ..                          [100%]


"""

### Pytest --cov report:

"""
    ---------- coverage: platform linux, python 3.12.1-final-0 -----------
    Name           Stmts   Miss  Cover
    ----------------------------------
    main.py            5      0   100%
    models.py         33      3    91%
    routes.py         17      0   100%
    test_main.py      27      0   100%
    ----------------------------------
    TOTAL             82      3    96%

    ========= 2 passed, 1 warning in 3.46s ========

"""
### Test Summary:
the pytest is a 100% indicating that all test cases works as intended, while the pytest coverage is 96% which is above the acceptance percentage score.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as per the terms of the license.