from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import SessionLocal
from app.schemas.detalle_venta_schema import DetalleVentaCreate, DetalleVentaOut
from app.services import detalle_venta_service

router = APIRouter(prefix="/detalles_venta", tags=["Detalles de Venta"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=DetalleVentaOut)
def crear_detalle_venta(detalle: DetalleVentaCreate, db: Session = Depends(get_db)):
    return detalle_venta_service.crear_detalle_venta_service(db, detalle)

@router.get("/", response_model=list[DetalleVentaOut])
def listar_detalles_venta(db: Session = Depends(get_db)):
    return detalle_venta_service.listar_detalles_venta_service(db)

@router.delete("/{detalle_id}", status_code=204)
def eliminar_detalle_venta(detalle_id: int, db: Session = Depends(get_db)):
    eliminado = detalle_venta_service.eliminar_detalle_venta_service(db, detalle_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Detalle de venta no encontrado")
    return None
