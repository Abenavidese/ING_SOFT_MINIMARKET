from sqlalchemy.orm import Session
from app.models.venta import Venta
from typing import List, Optional

def crear_venta(db: Session, venta: Venta) -> Venta:
    db.add(venta)
    db.commit()
    db.refresh(venta)
    return venta

def obtener_ventas(db: Session, cliente_id: Optional[str] = None) -> list[Venta]:
    query = db.query(Venta)
    if cliente_id:
        query = query.filter(Venta.cliente_id == cliente_id)
    return query.all()

def eliminar_venta(db: Session, venta_id: int) -> bool:
    venta = db.query(Venta).filter(Venta.id == venta_id).first()
    if venta:
        db.delete(venta)
        db.commit()
        return True
    return False

def actualizar_venta(db: Session, venta_id: int, data: dict) -> Venta:
    venta = db.query(Venta).filter(Venta.id == venta_id).first()
    if not venta:
        return None
    for key, value in data.items():
        setattr(venta, key, value)
    db.commit()
    db.refresh(venta)
    return venta
