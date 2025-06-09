"""
MiniMercado API
---------------
Backend para la gestión de un minimarket, desarrollado con FastAPI y SQLAlchemy.
Incluye módulos para la gestión de clientes, productos, ventas, proveedores, caja, categorías y detalles de venta.
"""

from fastapi import FastAPI
from app.config.database import Base, engine

# Importar modelos (asegura que las tablas se creen)
from app.models import producto, cliente, proveedor, categoria, venta, detalle_venta, caja

# Importar routers
from app.controllers.categoria_controller import router as categoria_router
from app.controllers.caja_controller import router as caja_router
from app.controllers.cliente_controller import router as cliente_router
from app.controllers.producto_controller import router as producto_router
from app.controllers.venta_controller import router as venta_router
from app.controllers.detalle_venta_controller import router as detalle_venta_router
from app.controllers.proveedor_controller import router as proveedor_router

# 1️⃣ Instanciar la aplicación
app = FastAPI(
    title="MiniMercado API",
    version="1.0",
    description="API REST para la gestión completa de un minimarket.",
    contact={
        "name": "Equipo MiniMarket",
        "email": "contacto@minimarket.com"
    }
)

# 2️⃣ Crear las tablas en la base de datos (si no existen)
Base.metadata.create_all(bind=engine)

# 3️⃣ Ruta base (health check)
@app.get("/")
def root():
    return {
        "mensaje": "✅ API del MiniMercado funcionando correctamente",
        "version": "1.0",
        "endpoints": "/docs"
    }

# 4️⃣ Incluir routers
app.include_router(categoria_router)
app.include_router(caja_router)
app.include_router(cliente_router)
app.include_router(producto_router)
app.include_router(venta_router)
app.include_router(detalle_venta_router)
app.include_router(proveedor_router)
