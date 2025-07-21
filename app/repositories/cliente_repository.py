from sqlalchemy.orm import Session
from app.models.cliente import Cliente

def crear_cliente(db: Session, cliente: Cliente) -> Cliente:
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return cliente

def obtener_todos_los_clientes(db: Session) -> list[Cliente]:
    return db.query(Cliente).all()

def eliminar_cliente(db: Session, cliente_id: str) -> bool:
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    if cliente:
        db.delete(cliente)
        db.commit()
        return True
    return False
