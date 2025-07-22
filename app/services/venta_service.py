from sqlalchemy.orm import Session
from fastapi import HTTPException
from typing import Optional
from app.models.venta import Venta
from app.schemas.venta_schema import VentaCreate, VentaUpdate
from app.repositories.venta_repository import crear_venta_con_detalles, obtener_ventas, eliminar_venta, actualizar_venta

def registrar_venta_service(venta_data: VentaCreate, db: Session) -> Venta:
    return crear_venta_con_detalles(
        db,
        cliente_id=venta_data.cliente_id,
        fecha=venta_data.fecha,
        detalles=[det.dict() for det in venta_data.detalles]
    )

def listar_ventas_service(db: Session, cliente_id: Optional[str] = None):
    return obtener_ventas(db, cliente_id)  # ahora acepta filtro por cliente

def eliminar_venta_service(venta_id: int, db: Session) -> bool:
    return eliminar_venta(db, venta_id)

def actualizar_venta_service(db: Session, venta_id: int, data: VentaUpdate) -> Venta:
    venta_actualizada = actualizar_venta(db, venta_id, data.dict(exclude_unset=True))
    if not venta_actualizada:
        raise HTTPException(status_code=404, detail="Venta no encontrada")
    return venta_actualizada
