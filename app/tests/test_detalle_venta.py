# tests/test_detalle_venta.py
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

def crear_producto():
    """
    Crea un producto de prueba.
    """
    resp = client.post("/productos/", json={
        "nombre": "Producto Test",
        "precio": 10.0,
        "stock": 100,
        "proveedor_id": 1,
        "categoria_id": 1
    })
    assert resp.status_code == 200

def crear_proveedor_y_categoria():
    """
    Crea un proveedor y una categoría de prueba.
    """
    # Crear proveedor
    resp = client.post("/proveedores/", json={
        "nombre": "Proveedor Test",
        "contacto": "123456789"  # campo correcto según tu ProveedorSchema
    })
    assert resp.status_code == 200

    # Crear categoría
    resp = client.post("/categorias/", json={
        "nombre": "Categoria Test"
    })
    assert resp.status_code == 200

def crear_venta():
    """
    Crea una venta de prueba.
    """
    resp = client.post("/ventas/", json={
        "cliente_id": 1,
        "total": 50.0
    })
    assert resp.status_code == 200

def crear_cliente():
    """
    Crea un cliente de prueba.
    """
    resp = client.post("/clientes/", json={
        "nombre": "Cliente Test",
        "email": "cliente@test.com",
        "telefono": "123456789",
        "frecuente": False
    })
    assert resp.status_code == 200

def test_crear_detalle_venta_y_listar(client):
    # Preparación: crear dependencias necesarias
    crear_proveedor_y_categoria()
    crear_producto()
    crear_cliente()
    crear_venta()

    # Crear detalle de venta
    payload = {
        "venta_id": 1,
        "producto_id": 1,
        "cantidad": 2,
        "precio_unitario": 10.0
    }
    resp = client.post("/detalles_venta/", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["id"] == 1
    assert data["venta_id"] == payload["venta_id"]
    assert data["producto_id"] == payload["producto_id"]
    assert data["cantidad"] == payload["cantidad"]
    assert data["precio_unitario"] == payload["precio_unitario"]

    # Listar detalles de venta
    resp = client.get("/detalles_venta/")
    assert resp.status_code == 200
    lista = resp.json()
    assert isinstance(lista, list)
    assert len(lista) == 1
    assert lista[0]["venta_id"] == payload["venta_id"]

def test_actualizar_detalle_venta(client):
    # Preparación
    crear_proveedor_y_categoria()
    crear_producto()
    crear_cliente()
    crear_venta()

    client.post("/detalles_venta/", json={
        "venta_id": 1,
        "producto_id": 1,
        "cantidad": 3,
        "precio_unitario": 15.0
    })

    # Actualizar cantidad y precio
    update_payload = {
        "cantidad": 5,
        "precio_unitario": 20.0
    }
    resp = client.put("/detalles_venta/1", json=update_payload)
    assert resp.status_code == 200
    updated = resp.json()
    assert updated["cantidad"] == 5
    assert updated["precio_unitario"] == 20.0

def test_eliminar_detalle_venta(client):
    # Preparación
    crear_proveedor_y_categoria()
    crear_producto()
    crear_cliente()
    crear_venta()

    client.post("/detalles_venta/", json={
        "venta_id": 1,
        "producto_id": 1,
        "cantidad": 1,
        "precio_unitario": 5.0
    })

    # Eliminar
    resp = client.delete("/detalles_venta/1")
    assert resp.status_code == 204

    # Lista vacía
    resp = client.get("/detalles_venta/")
    assert resp.status_code == 200
    assert resp.json() == []
