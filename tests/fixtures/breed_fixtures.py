import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def breed_data_1():
    return {"name": "Siamese", "description": "A breed of cat from Thailand"}


@pytest.fixture
def breed_data_2():
    return {"name": "Persian", "description": "A breed of cat with long fur"}


@pytest.fixture
def created_breed_1(client: TestClient, breed_data_1: dict) -> dict:
    response = client.post("/breeds/", json=breed_data_1)
    assert response.status_code == 200
    return response.json()


@pytest.fixture
def created_breed_2(client: TestClient, breed_data_2: dict) -> dict:
    response = client.post("/breeds/", json=breed_data_2)
    assert response.status_code == 200
    return response.json()
