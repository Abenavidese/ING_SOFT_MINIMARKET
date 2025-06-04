from sqlalchemy.orm import Session
from app.models.venta import Venta
from typing import List

def crear_venta(db: Session, venta: Venta) -> Venta:
    db.add(venta)
    db.commit()
    db.refresh(venta)
    return venta

def obtener_ventas(db: Session) -> List[Venta]:
    return db.query(Venta).all()

def eliminar_venta(db: Session, venta_id: int) -> bool:
    venta = db.query(Venta).filter(Venta.id == venta_id).first()
    if venta:
        db.delete(venta)
        db.commit()
        return True
    return False
