from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.caja import Caja
from app.schemas.caja_schema import CajaCreate, CajaUpdate
from app.repositories import caja_repository
from sqlalchemy import func
from datetime import date
from app.models.venta import Venta

def crear_caja_service(db: Session, caja_data: CajaCreate) -> Caja:
    nueva_caja = Caja(**caja_data.model_dump())
    return caja_repository.crear_caja(db, nueva_caja)

def listar_cajas_service(db: Session) -> list[Caja]:
    return caja_repository.obtener_todas_las_cajas(db)

def eliminar_caja_service(db: Session, caja_id: int) -> bool:
    return caja_repository.eliminar_caja(db, caja_id)

def actualizar_caja_service(db: Session, caja_id: int, data: CajaUpdate) -> Caja:
    caja = db.query(Caja).filter(Caja.id == caja_id).first()
    if not caja:
        raise HTTPException(status_code=404, detail="Caja no encontrada")

    for key, value in data.model_dump().items():
        setattr(caja, key, value)

    db.commit()
    db.refresh(caja)
    return caja

def obtener_caja_con_total_dinamico(db: Session, fecha: date) -> dict:
    caja = db.query(Caja).filter(Caja.fecha == fecha).first()
    if not caja:
        raise HTTPException(status_code=404, detail="Caja no encontrada para la fecha")

    total_ventas = db.query(func.sum(Venta.total)).filter(Venta.fecha == fecha).scalar() or 0.0

    return {
        "id": caja.id,
        "fecha": caja.fecha,
        "estado": caja.estado,
        "total_dia": total_ventas
    }