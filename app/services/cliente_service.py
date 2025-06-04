from sqlalchemy.orm import Session
from app.schemas.cliente_schema import ClienteCreate
from app.models.cliente import Cliente
from app.repositories.cliente_repository import crear_cliente, obtener_todos_los_clientes

# Servicio para crear un cliente
def crear_cliente_service(cliente_data: ClienteCreate, db: Session) -> Cliente:
    nuevo_cliente = Cliente(**cliente_data.model_dump())  # ← cambio aquí
    return crear_cliente(db, nuevo_cliente)

# Servicio para listar todos los clientes
def listar_clientes_service(db: Session) -> list[Cliente]:
    return obtener_todos_los_clientes(db)
