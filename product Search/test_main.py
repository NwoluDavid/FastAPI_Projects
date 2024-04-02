from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World"}


def test_read_product_with_all_parameters():
    response = client.get("/product?product_name=laptop&category=Electronics&price_range=1000_1500")
    assert response.status_code == 200
    assert len(response.json()["product"]) == 1


def test_read_product_with_product_name():
    response = client.get("/product?product_name=laptop")
    assert response.status_code == 200
    assert len(response.json()["product"]) == 1


def test_read_product_with_category():
    response = client.get("/product?category=Appliances")
    assert response.status_code == 200
    assert len(response.json()["product"]) == 1


def test_read_product_with_price_range():
    response = client.get("/product?price_range=0_100")
    assert response.status_code == 200
    assert len(response.json()["product"]) == 7


