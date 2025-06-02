from fastapi import FastAPI
from app.config.database import Base, engine

# Importa los modelos
from app.models import producto, cliente, proveedor, categoria, venta, detalle_venta, caja

# Importa los routers
from app.controllers.categoria_controller import router as categoria_router
from app.controllers.caja_controller import router as caja_router  # caja añadida

# 1. Instancia de la app
app = FastAPI(title="MiniMercado API", version="1.0")

# 2. Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# 3. Ruta base
@app.get("/")
def root():
    return {"mensaje": "API del MiniMercado funcionando correctamente"}

# 4. Routers
app.include_router(categoria_router)
app.include_router(caja_router)  #  incluir el router de caja
