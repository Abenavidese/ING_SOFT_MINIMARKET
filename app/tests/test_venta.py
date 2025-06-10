import pytest
from fastapi.testclient import TestClient
from app.main import app
from datetime import date
client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_db():
    from app.config.database import Base, engine
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_crear_y_listar_venta(client):
    # Asegúrate de tener un cliente con ID 1 ya creado, o crear uno aquí
    resp = client.post("/ventas/", json={
        "cliente_id": 1,
        "total": 100.00
    })
    assert resp.status_code == 200
    assert resp.json()["total"] == 100.00

    resp = client.get("/ventas/")
    assert resp.status_code == 200
    assert len(resp.json()) == 1

def test_actualizar_venta(client):
    client.post("/ventas/", json={
        "cliente_id": 1,
        "total": 100.00
    })
    resp = client.put("/ventas/1", json={
        "cliente_id": 1,
        "total": 200.00,
        "fecha": str(date.today())  # Agregamos fecha como string
    })
    assert resp.status_code == 200
    assert resp.json()["total"] == 200.00

def test_eliminar_venta(client):
    client.post("/ventas/", json={
        "cliente_id": 1,
        "total": 50.00
    })
    resp = client.delete("/ventas/1")
    assert resp.status_code == 204

    resp = client.get("/ventas/")
    assert resp.status_code == 200
    assert resp.json() == []
