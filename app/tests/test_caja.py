# tests/test_caja.py

import pytest
from fastapi.testclient import TestClient
from app.main import app
from datetime import date

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_db():
    """
    Se ejecuta antes de cada test: limpia y crea de nuevo tablas.
    """
    from app.config.database import Base, engine
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_crear_caja_y_listar(client):
    # 1) Crear una caja
    payload = {
        "fecha": str(date.today()),
        "estado": "Abierta",
        "total_dia": 100.50
    }
    resp = client.post("/cajas/", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["id"] == 1
    assert data["estado"] == payload["estado"]
    assert data["total_dia"] == payload["total_dia"]

    # 2) Listar cajas y comprobar que aparece
    resp = client.get("/cajas/")
    assert resp.status_code == 200
    lista = resp.json()
    assert isinstance(lista, list)
    assert len(lista) == 1
    assert lista[0]["estado"] == payload["estado"]

def test_actualizar_caja(client):
    # Previamente crear una caja
    client.post("/cajas/", json={
        "fecha": str(date.today()),
        "estado": "Abierta",
        "total_dia": 50.00
    })

    # Actualizar la caja
    update_payload = {
        "fecha": str(date.today()),
        "estado": "Cerrada",
        "total_dia": 150.00
    }
    resp = client.put("/cajas/1", json=update_payload)
    assert resp.status_code == 200
    updated = resp.json()
    assert updated["estado"] == "Cerrada"
    assert updated["total_dia"] == 150.00

def test_eliminar_caja(client):
    # Crear una caja
    client.post("/cajas/", json={
        "fecha": str(date.today()),
        "estado": "Abierta",
        "total_dia": 80.00
    })

    # Eliminar la caja
    resp = client.delete("/cajas/1")
    assert resp.status_code == 204

    # La lista de cajas debe estar vacía
    resp = client.get("/cajas/")
    assert resp.status_code == 200
    assert resp.json() == []
