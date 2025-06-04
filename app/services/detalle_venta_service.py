from sqlalchemy.orm import Session
from app.models.detalle_venta import DetalleVenta
from app.schemas.detalle_venta_schema import DetalleVentaCreate
from app.repositories import detalle_venta_repository

def crear_detalle_venta_service(db: Session, data: DetalleVentaCreate) -> DetalleVenta:
    nuevo = DetalleVenta(**data.model_dump())
    return detalle_venta_repository.crear_detalle_venta(db, nuevo)

def listar_detalles_venta_service(db: Session):
    return detalle_venta_repository.listar_detalles_venta(db)

def eliminar_detalle_venta_service(db: Session, detalle_id: int) -> bool:
    return detalle_venta_repository.eliminar_detalle_venta(db, detalle_id)
