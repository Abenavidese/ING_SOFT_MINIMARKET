from sqlalchemy.orm import Session
from app.models.cliente import Cliente

def crear_cliente(db: Session, cliente: Cliente) -> Cliente:
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return cliente

def obtener_todos_los_clientes(db: Session) -> list[Cliente]:
    return db.query(Cliente).all()
