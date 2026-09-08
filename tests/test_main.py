from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_hello():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello FastAPI"}


def test_path_and_query():
    assert client.get("/items/7?q=book").json() == {"item_id": 7, "q": "book"}
    assert client.get("/items/not-a-number").status_code == 422


def test_body_validation():
    response = client.post("/items/", json={"name": "book", "price": 12.5})
    assert response.status_code == 201
    assert response.json() == {"name": "book", "price": 12.5}
    assert client.post("/items/", json={"name": "book", "price": -1}).status_code == 422
