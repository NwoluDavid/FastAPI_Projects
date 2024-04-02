## Product Search API with FastAPI

**Author:** David Nwolu

**License:** MIT

This FastAPI project implements a powerful search endpoint for products. It allows users to filter products based on various criteria using query parameters, making product discovery efficient.

### Key Features

* **Search by name, category, and price range:** Refine your product search using flexible query parameters.
* **Data validation:** Ensures data integrity with built-in validation for parameters like name, category, and price range.
* **Clear and concise response:** Get a well-structured JSON response containing matching products.


### Technologies

- Python 3.7+
- FastAPI
- Pydantic (for data validation)

### Installation

1. Clone this repository:

```bash
git clone https://github.com/NwoluDavid/FastAPI_Projects/tree/staging/product%20Search>
```

2. Navigate to the project directory:

```bash
cd product-search-api
```

3. Install dependencies using pip:

```bash
pip install -r requirements.txt
```

### Usage

1. Run the FastAPI server:

```bash
uvicorn main:app --reload
```

2. The API will be running on `http://localhost:8000`.

3. Use tools like Postman or curl to send requests to the API endpoints.

### Endpoints

**GET /products**

Searches for products based on query parameters.

**Query Parameters:**

* `name` (str, optional): Filter by product name. String validation is applied.
* `category` (str, optional): Filter by product category. String validation is applied.
* `min_price` (float, optional): Set the minimum price for the search range.
* `max_price` (float, optional): Set the maximum price for the search range.

**Returns:**

A JSON list of products matching the search criteria.

### Examples

**Search for products by name and category:**

```bash
curl -X GET "http://localhost:8000/products?name=iphone&category=electronics"
```

**Search for products within a price range:**

```bash
curl -X GET "http://localhost:8000/products?min_price=100&max_price=500"
```

**Search for products with all filters:**

```bash
curl -X GET "http://localhost:8000/products?name=iphone&category=electronics&min_price=100&max_price=500"
```

### Response Example

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

### Contributing

We welcome contributions to this project! Feel free to open an issue or submit a pull request.

### License

This project is licensed under the MIT License ([https://opensource.org/license/mit](https://opensource.org/license/mit)). You are free to use, modify, and distribute it according to the license terms.

### Test Reports

Test reports including pytest coverage (`coverage` library) are available within the project to ensure code quality.
