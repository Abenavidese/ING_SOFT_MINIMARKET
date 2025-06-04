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

def eliminar_producto(db: Session, producto_id: int) -> bool:
    producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if producto:
        db.delete(producto)
        db.commit()
        return True
    return False
