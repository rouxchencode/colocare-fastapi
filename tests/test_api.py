from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_list_foods():
    response = client.get("/foods/")
    assert response.status_code == 200

def test_get_food_not_found():
    response = client.get("/foods/99999")
    assert response.status_code == 404


def test_get_food_search():
    response = client.get("/foods/search", params={"keyword": "米"})
    assert response.status_code == 200

def test_post_food():
    response = client.post("/foods/", json= {
    "food_name": "測試白飯",
    "crude_fiber": 0.5,
    "fat_ratio": 1.2,
    "gas_label": False
})
    assert response.status_code == 201
    assert response.json()["food_name"] == "測試白飯"