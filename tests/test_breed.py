from fastapi.testclient import TestClient
from tests.fixtures import *


def test_create_breed(client: TestClient, breed_data_1: dict) -> None:
    response = client.post("/breeds/", json=breed_data_1)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == breed_data_1["name"]
    assert data["description"] == breed_data_1["description"]
    assert "id" in data


def test_get_all_breeds(client: TestClient, created_breed_1: dict) -> None:
    response = client.get("/breeds/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert data[0]["name"] == created_breed_1["name"]


def test_get_breed_by_id(client: TestClient, created_breed_1: dict) -> None:
    breed_id = created_breed_1["id"]
    response = client.get(f"/breeds/{breed_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == breed_id
    assert data["name"] == created_breed_1["name"]


def test_update_breed(client: TestClient, created_breed_1: dict) -> None:
    breed_id = created_breed_1["id"]
    updated_data = {"name": "Updated Breed", "description": "Updated Description"}
    update_response = client.put(f"/breeds/{breed_id}", json=updated_data)
    assert update_response.status_code == 200
    data = update_response.json()
    assert data["name"] == updated_data["name"]
    assert data["description"] == updated_data["description"]


def test_delete_breed(client: TestClient, created_breed_1: dict) -> None:
    breed_id = created_breed_1["id"]
    delete_response = client.delete(f"/breeds/{breed_id}")
    assert delete_response.status_code == 200
    data = delete_response.json()
    assert data["message"] == "Breed successfully deleted"
    get_response = client.get(f"/breeds/{breed_id}")
    assert get_response.status_code == 404
