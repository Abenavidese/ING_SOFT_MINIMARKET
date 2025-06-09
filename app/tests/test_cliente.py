# tests/test_cliente.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

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

def test_crear_cliente_y_listar(client):
    # 1) Crear un cliente
    payload = {
        "nombre": "Carlos López",
        "email": "carlos@correo.com",
        "telefono": "0991234567",
        "frecuente": True
    }
    resp = client.post("/clientes/", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["id"] == 1
    assert data["nombre"] == payload["nombre"]
    assert data["frecuente"] is True

    # 2) Listar clientes y comprobar que aparece
    resp = client.get("/clientes/")
    assert resp.status_code == 200
    lista = resp.json()
    assert isinstance(lista, list)
    assert len(lista) == 1
    assert lista[0]["email"] == payload["email"]

def test_actualizar_cliente(client):
    # Previamente creamos
    client.post("/clientes/", json={
        "nombre": "Ana Pérez",
        "email": "ana@correo.com",
        "telefono": "0987654321",
        "frecuente": False
    })

    # Actualizar sólo el campo 'frecuente'
    update_payload = { "frecuente": True }
    resp = client.put("/clientes/1", json=update_payload)
    assert resp.status_code == 200
    updated = resp.json()
    assert updated["frecuente"] is True
    assert updated["nombre"] == "Ana Pérez"  # resto inalterado

def test_eliminar_cliente(client):
    # Crear y luego eliminar
    client.post("/clientes/", json={
        "nombre": "Luis Ramírez",
        "email": "luis@correo.com",
        "telefono": "0970000000",
        "frecuente": False
    })
    # Delete
    resp = client.delete("/clientes/1")
    assert resp.status_code == 204

    # Ahora la lista debe estar vacía
    resp = client.get("/clientes/")
    assert resp.status_code == 200
    assert resp.json() == []
