import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def kitten_data_1(created_breed_1: dict):
    return {
        "name": "Fluffy",
        "color": "white",
        "age_months": 3,
        "description": "A cute white kitten",
        "breed_id": created_breed_1["id"],
    }


@pytest.fixture
def kitten_data_2(created_breed_2: dict):
    return {
        "name": "Shadow",
        "color": "black",
        "age_months": 4,
        "description": "A mysterious black kitten",
        "breed_id": created_breed_2["id"],
    }


@pytest.fixture
def created_kitten_1(client: TestClient, kitten_data_1: dict) -> dict:
    response = client.post("/kittens/", json=kitten_data_1)
    assert response.status_code == 200
    return response.json()


@pytest.fixture
def created_kitten_2(client: TestClient, kitten_data_2: dict) -> dict:
    response = client.post("/kittens/", json=kitten_data_2)
    assert response.status_code == 200
    return response.json()
