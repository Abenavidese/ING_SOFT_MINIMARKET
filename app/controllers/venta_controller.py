from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import SessionLocal
from app.schemas.venta_schema import VentaCreate, VentaOut
from app.services.venta_service import registrar_venta_service, listar_ventas_service

router = APIRouter(prefix="/ventas", tags=["Ventas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=VentaOut)
def registrar_venta(venta: VentaCreate, db: Session = Depends(get_db)):
    return registrar_venta_service(venta, db)

@router.get("/", response_model=list[VentaOut])
def listar_ventas(db: Session = Depends(get_db)):
    return listar_ventas_service(db)
