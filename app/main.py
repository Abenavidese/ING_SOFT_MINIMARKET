from fastapi import FastAPI
from app.config.database import Base, engine

# Importa TODOS los modelos aquí
from app.models import producto, cliente, proveedor, categoria, venta, detalle_venta, caja

app = FastAPI()

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)
