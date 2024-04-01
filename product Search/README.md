# Product Search API

This project implements a FastAPI endpoint for searching products. It accepts query parameters for product name, category, and price range, allowing users to filter products based on these criteria. String validation is applied for the product name and category, while numeric validation is applied for the price range parameters. The API returns a list of products matching the search criteria.

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
    cd product-search-api
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

- **GET /products:** Search for products based on query parameters.
    - Query parameters: `name`, `category`, `min_price`, `max_price`.
    - Returns a list of products matching the search criteria.

## Examples

### Search for products by name and category

```bash
curl -X GET "http://localhost:8000/products?name=iphone&category=electronics"
```

### Search for products within a price range

```bash
curl -X GET "http://localhost:8000/products?min_price=100&max_price=500"
```

### Search for products by name, category, and price range

```bash
curl -X GET "http://localhost:8000/products?name=iphone&category=electronics&min_price=100&max_price=500"
```

### Example Response

```json
[
    {
        "id": 1,
        "name": "iPhone X",
        "category": "Electronics",
        "price": 999.99
    },
    {
        "id": 2,
        "name": "Samsung Galaxy S20",
        "category": "Electronics",
        "price": 799.99
    }
]
```

## Documentation

Additional documentation or resources related to this project will be available soon.

## Contributing

If you'd like to contribute to this project, feel free to open an issue or submit a pull request. Contributions are always welcome!

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as per the terms of the license.