import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_db():
    from app.config.database import Base, engine
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_crear_y_listar_proveedor(client):
    resp = client.post("/proveedores/", json={
        "nombre": "Proveedor X",
        "contacto": "0999999999"
    })
    assert resp.status_code == 200
    data = resp.json()
    assert data["nombre"] == "Proveedor X"

    resp = client.get("/proveedores/")
    assert resp.status_code == 200
    assert len(resp.json()) == 1

def test_actualizar_proveedor(client):
    client.post("/proveedores/", json={
        "nombre": "Proveedor Inicial",
        "contacto": "0000000000"
    })
    resp = client.put("/proveedores/1", json={
        "nombre": "Proveedor Actualizado",
        "contacto": "1234567890"
    })
    assert resp.status_code == 200
    assert resp.json()["nombre"] == "Proveedor Actualizado"

def test_eliminar_proveedor(client):
    client.post("/proveedores/", json={
        "nombre": "A Eliminar",
        "contacto": "0000000000"
    })
    resp = client.delete("/proveedores/1")
    assert resp.status_code == 204

    resp = client.get("/proveedores/")
    assert resp.json() == []
