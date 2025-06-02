from fastapi import FastAPI
from app.config.database import Base, engine
from app.models import producto, cliente, proveedor, categoria, venta, detalle_venta, caja
from app.controllers.categoria_controller import router as categoria_router  # 👈 importar router

# 1. Instancia de la app
app = FastAPI(title="MiniMercado API", version="1.0")

# 2. Crear las tablas en la base de datos (solo la primera vez)
Base.metadata.create_all(bind=engine)

# 3. Ruta de prueba
@app.get("/")
def root():
    return {"mensaje": "API del MiniMercado funcionando correctamente"}

# 4. Incluir router de categorías (ya listo)
app.include_router(categoria_router)
