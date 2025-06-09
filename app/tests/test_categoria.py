# tests/test_categoria.py
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

def test_crear_categoria_y_listar(client):
    # 1) Crear una categoría
    payload = {
        "nombre": "Bebidas"
    }
    resp = client.post("/categorias/", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["id"] == 1
    assert data["nombre"] == payload["nombre"]

    # 2) Listar categorías y comprobar que aparece
    resp = client.get("/categorias/")
    assert resp.status_code == 200
    lista = resp.json()
    assert isinstance(lista, list)
    assert len(lista) == 1
    assert lista[0]["nombre"] == payload["nombre"]

def test_actualizar_categoria(client):
    # Previamente creamos
    client.post("/categorias/", json={ "nombre": "Snacks" })

    # Actualizar nombre
    update_payload = { "nombre": "Snacks y golosinas" }
    resp = client.put("/categorias/1", json=update_payload)
    assert resp.status_code == 200
    updated = resp.json()
    assert updated["nombre"] == update_payload["nombre"]

def test_eliminar_categoria(client):
    # Crear y luego eliminar
    client.post("/categorias/", json={ "nombre": "Lácteos" })

    # Delete
    resp = client.delete("/categorias/1")
    assert resp.status_code == 204

    # Ahora la lista debe estar vacía
    resp = client.get("/categorias/")
    assert resp.status_code == 200
    assert resp.json() == []
