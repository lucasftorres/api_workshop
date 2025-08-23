import pytest

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200

def test_read_root_json():
    response = client.get("/")
    assert response.json() == {"Hello": "World"}

def test_listar_produtos():
    response = client.get("/produtos")
    assert response.status_code == 200

def test_tamanho_lista_produtos():
    response = client.get("/produtos")
    assert len(response.json()) == 3