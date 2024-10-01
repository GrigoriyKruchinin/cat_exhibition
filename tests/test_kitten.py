from fastapi.testclient import TestClient
from tests.fixtures import *


def test_create_kitten(client: TestClient, kitten_data_1: dict) -> None:
    response = client.post("/kittens/", json=kitten_data_1)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == kitten_data_1["name"]
    assert data["color"] == kitten_data_1["color"]
    assert data["age_months"] == kitten_data_1["age_months"]
    assert data["description"] == kitten_data_1["description"]
    assert data["breed_id"] == kitten_data_1["breed_id"]
    assert "id" in data


def test_get_all_kittens(client: TestClient, created_kitten_1: dict) -> None:
    response = client.get("/kittens/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert data[0]["name"] == created_kitten_1["name"]


def test_get_kitten_by_id(client: TestClient, created_kitten_1: dict) -> None:
    kitten_id = created_kitten_1["id"]
    response = client.get(f"/kittens/{kitten_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == kitten_id
    assert data["name"] == created_kitten_1["name"]


def test_update_kitten(client: TestClient, created_kitten_1: dict) -> None:
    kitten_id = created_kitten_1["id"]
    updated_data = {
        "name": "Updated Kitten",
        "color": "gray",
        "age_months": 5,
        "description": "Updated Description",
        "breed_id": created_kitten_1["breed_id"],
    }
    update_response = client.put(f"/kittens/{kitten_id}", json=updated_data)
    assert update_response.status_code == 200
    data = update_response.json()
    assert data["name"] == updated_data["name"]
    assert data["color"] == updated_data["color"]
    assert data["age_months"] == updated_data["age_months"]
    assert data["description"] == updated_data["description"]


def test_delete_kitten(client: TestClient, created_kitten_1: dict) -> None:
    kitten_id = created_kitten_1["id"]
    delete_response = client.delete(f"/kittens/{kitten_id}")
    assert delete_response.status_code == 200
    data = delete_response.json()
    assert data["message"] == "Kitten successfully deleted"
    get_response = client.get(f"/kittens/{kitten_id}")
    assert get_response.status_code == 404
