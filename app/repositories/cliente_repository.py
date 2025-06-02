from sqlalchemy.orm import Session
from app.models.cliente import Cliente

def crear_cliente(db: Session, cliente_data: dict) -> Cliente:
    cliente = Cliente(**cliente_data)
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return cliente

def listar_clientes(db: Session) -> list[Cliente]:
    return db.query(Cliente).all()
