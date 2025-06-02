from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import SessionLocal
from app.models.venta import Venta
from app.models.detalle_venta import DetalleVenta
from app.schemas.venta_schema import VentaCreate, VentaOut
from app.schemas.detalle_venta_schema import DetalleVentaCreate

router = APIRouter(prefix="/ventas", tags=["Ventas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=VentaOut)
def registrar_venta(venta: VentaCreate, db: Session = Depends(get_db)):
    nueva_venta = Venta(
        cliente_id=venta.cliente_id,
        total=venta.total
    )
    db.add(nueva_venta)
    db.commit()
    db.refresh(nueva_venta)

    # Puedes agregar detalles aquí si ya tienes una estructura más avanzada
    return nueva_venta

@router.get("/", response_model=list[VentaOut])
def listar_ventas(db: Session = Depends(get_db)):
    return db.query(Venta).all()
