from sqlalchemy.orm import Session
from app.models.detalle_venta import DetalleVenta
from app.schemas.detalle_venta_schema import DetalleVentaCreate
from app.repositories import detalle_venta_repository
from app.schemas.detalle_venta_schema import DetalleVentaUpdate

def crear_detalle_venta_service(db: Session, data: DetalleVentaCreate) -> DetalleVenta:
    nuevo = DetalleVenta(**data.model_dump())
    return detalle_venta_repository.crear_detalle_venta(db, nuevo)

def listar_detalles_venta_service(db: Session):
    return detalle_venta_repository.listar_detalles_venta(db)

def eliminar_detalle_venta_service(db: Session, detalle_id: int) -> bool:
    return detalle_venta_repository.eliminar_detalle_venta(db, detalle_id)

def actualizar_detalle_service(db: Session, detalle_id: int, data: DetalleVentaUpdate):
    detalle = detalle_venta_repository.obtener_detalle_venta_por_id(db, detalle_id)
    if not detalle:
        return None
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(detalle, key, value)
    db.commit()
    db.refresh(detalle)
    return detalle