from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from app.config.database import SessionLocal
from app.schemas.venta_schema import VentaCreate, VentaOut, VentaUpdate
from app.services.venta_service import (
    registrar_venta_service,
    listar_ventas_service,
    eliminar_venta_service,
    actualizar_venta_service
)

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

@router.get("/", response_model=List[VentaOut])
def listar_ventas(cliente_id: Optional[str] = None, db: Session = Depends(get_db)):
    return listar_ventas_service(db, cliente_id)  # Llama al service correcto

@router.delete("/{venta_id}", status_code=204)
def eliminar_venta(venta_id: int, db: Session = Depends(get_db)):
    eliminado = eliminar_venta_service(venta_id, db)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Venta no encontrada")
    return None  # 204 No Content

@router.put("/{venta_id}", response_model=VentaOut)
def actualizar_venta(venta_id: int, data: VentaUpdate, db: Session = Depends(get_db)):
    return actualizar_venta_service(db, venta_id, data)
