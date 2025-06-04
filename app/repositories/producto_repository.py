from sqlalchemy.orm import Session
from app.models.producto import Producto

def crear_producto(db: Session, producto_data: dict) -> Producto:
    producto = Producto(**producto_data)
    db.add(producto)
    db.commit()
    db.refresh(producto)
    return producto

def listar_productos(db: Session) -> list[Producto]:
    return db.query(Producto).all()
