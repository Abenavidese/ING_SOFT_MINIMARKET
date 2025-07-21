from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.schemas.cliente_schema import ClienteCreate, ClienteUpdate
from app.models.cliente import Cliente
from app.repositories.cliente_repository import crear_cliente, obtener_todos_los_clientes, eliminar_cliente 

# Servicio para crear un cliente
def crear_cliente_service(cliente_data: ClienteCreate, db: Session) -> Cliente:
    nuevo_cliente = Cliente(**cliente_data.model_dump())  # id = UID de Firebase
    return crear_cliente(db, nuevo_cliente)

# Servicio para listar todos los clientes
def listar_clientes_service(db: Session) -> list[Cliente]:
    return obtener_todos_los_clientes(db)

# Servicio para eliminar un cliente
def eliminar_cliente_service(cliente_id: str, db: Session) -> bool:
    return eliminar_cliente(db, cliente_id)

# Servicio para actualizar un cliente
def actualizar_cliente_service(db: Session, cliente_id: str, data: ClienteUpdate) -> Cliente:
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")

    # Solo actualizar campos enviados
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(cliente, key, value)

    db.commit()
    db.refresh(cliente)
    return cliente
