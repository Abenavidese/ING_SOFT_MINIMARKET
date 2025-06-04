from fastapi import FastAPI
from app.config.database import Base, engine

# Importar modelos
from app.models import producto, cliente, proveedor, categoria, venta, detalle_venta, caja

# Importar routers
from app.controllers.categoria_controller import router as categoria_router
from app.controllers.caja_controller import router as caja_router
from app.controllers.cliente_controller import router as cliente_router
from app.controllers.producto_controller import router as producto_router
from app.controllers.venta_controller import router as venta_router
from app.controllers.detalle_venta_controller import router as detalle_venta_router
from app.controllers.proveedor_controller import router as proveedor_router

# 1. Instanciar la aplicación
app = FastAPI(title="MiniMercado API", version="1.0")

# 2. Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# 3. Ruta base de prueba
@app.get("/")
def root():
    return {"mensaje": "API del MiniMercado funcionando correctamente"}

# 4. Incluir routers
app.include_router(categoria_router)
app.include_router(caja_router)
app.include_router(cliente_router)
app.include_router(producto_router)
app.include_router(venta_router)
app.include_router(detalle_venta_router)
app.include_router(proveedor_router)
