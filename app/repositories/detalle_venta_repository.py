from sqlalchemy.orm import Session
from app.models.detalle_venta import DetalleVenta
from typing import List

def crear_detalle_venta(db: Session, detalle: DetalleVenta) -> DetalleVenta:
    db.add(detalle)
    db.commit()
    db.refresh(detalle)
    return detalle

def listar_detalles_venta(db: Session) -> List[DetalleVenta]:
    return db.query(DetalleVenta).all()

def eliminar_detalle_venta(db: Session, detalle_id: int) -> bool:
    detalle = db.query(DetalleVenta).filter(DetalleVenta.id == detalle_id).first()
    if detalle:
        db.delete(detalle)
        db.commit()
        return True
    return False

def obtener_detalle_venta_por_id(db: Session, detalle_id: int):
    return db.query(DetalleVenta).filter(DetalleVenta.id == detalle_id).first()

def actualizar_detalle_venta(db: Session, detalle_id: int, data: dict) -> DetalleVenta | None:
    detalle = obtener_detalle_por_id(db, detalle_id)
    if not detalle:
        return None
    for key, value in data.items():
        setattr(detalle, key, value)
    db.commit()
    db.refresh(detalle)
    return detalle
