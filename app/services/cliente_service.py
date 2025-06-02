from sqlalchemy.orm import Session
from app.repositories import cliente_repository
from app.schemas.cliente_schema import ClienteCreate

def crear_cliente_service(db: Session, cliente: ClienteCreate):
    return cliente_repository.crear_cliente(db, cliente.dict())

def listar_clientes_service(db: Session):
    return cliente_repository.listar_clientes(db)
