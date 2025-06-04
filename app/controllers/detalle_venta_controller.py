from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import SessionLocal
from app.models.detalle_venta import DetalleVenta
from app.schemas.detalle_venta_schema import DetalleVentaCreate, DetalleVentaOut

router = APIRouter(prefix="/detalles_venta", tags=["Detalles de Venta"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=DetalleVentaOut)
def crear_detalle_venta(detalle: DetalleVentaCreate, db: Session = Depends(get_db)):
    nuevo_detalle = DetalleVenta(**detalle.model_dump())  
    db.add(nuevo_detalle)
    db.commit()
    db.refresh(nuevo_detalle)
    return nuevo_detalle

@router.get("/", response_model=list[DetalleVentaOut])
def listar_detalles_venta(db: Session = Depends(get_db)):
    return db.query(DetalleVenta).all()
