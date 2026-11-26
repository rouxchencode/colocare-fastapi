from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_list_foods():
    response = client.get("/foods/")
    assert response.status_code == 200

def test_get_food_not_found():
    response = client.get("/foods/99999")
    assert response.status_code == 404