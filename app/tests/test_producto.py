# tests/test_producto.py
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

def crear_proveedor_y_categoria():
    # crear proveedor
    resp = client.post("/proveedores/", json={
        "nombre": "Proveedor Test",
        "contacto": "123456789"
    })
    assert resp.status_code == 200

    # crear categoria
    resp = client.post("/categorias/", json={
        "nombre": "Categoria Test"
    })
    assert resp.status_code == 200

def test_crear_producto_y_listar(client):
    crear_proveedor_y_categoria()

    payload = {
        "nombre": "Producto Test",
        "precio": 25.0,
        "stock": 50,
        "proveedor_id": 1,
        "categoria_id": 1
    }

    resp = client.post("/productos/", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["id"] == 1
    assert data["nombre"] == payload["nombre"]
    assert data["precio"] == payload["precio"]
    assert data["stock"] == payload["stock"]

    # Listar productos
    resp = client.get("/productos/")
    assert resp.status_code == 200
    lista = resp.json()
    assert isinstance(lista, list)
    assert len(lista) == 1
    assert lista[0]["nombre"] == payload["nombre"]

def test_actualizar_producto(client):
    crear_proveedor_y_categoria()

    # Crear producto
    client.post("/productos/", json={
        "nombre": "Producto Original",
        "precio": 30.0,
        "stock": 100,
        "proveedor_id": 1,
        "categoria_id": 1
    })

    # Actualizar precio y stock
    update_payload = {
        "nombre": "Producto Modificado",
        "precio": 35.0,
        "stock": 80,
        "proveedor_id": 1,
        "categoria_id": 1
    }

    resp = client.put("/productos/1", json=update_payload)
    assert resp.status_code == 200
    updated = resp.json()
    assert updated["nombre"] == "Producto Modificado"
    assert updated["precio"] == 35.0
    assert updated["stock"] == 80

def test_eliminar_producto(client):
    crear_proveedor_y_categoria()

    # Crear producto
    client.post("/productos/", json={
        "nombre": "Producto a eliminar",
        "precio": 15.0,
        "stock": 20,
        "proveedor_id": 1,
        "categoria_id": 1
    })

    # Eliminar
    resp = client.delete("/productos/1")
    assert resp.status_code == 204

    # Lista vacía
    resp = client.get("/productos/")
    assert resp.status_code == 200
    assert resp.json() == []
