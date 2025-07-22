from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.config.database import SessionLocal
from app.schemas.caja_schema import CajaCreate, CajaOut
from app.services import caja_service
from app.schemas.caja_schema import CajaUpdate
from app.services.caja_service import actualizar_caja_service, obtener_caja_con_total_dinamico
from datetime import date

router = APIRouter(prefix="/cajas", tags=["Cajas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=CajaOut)
def abrir_caja(caja: CajaCreate, db: Session = Depends(get_db)):
    return caja_service.crear_caja_service(db, caja)

@router.get("/", response_model=list[CajaOut])
def listar_cajas(db: Session = Depends(get_db)):
    return caja_service.listar_cajas_service(db)

@router.delete("/{caja_id}", status_code=204)
def eliminar_caja(caja_id: int, db: Session = Depends(get_db)):
    eliminada = caja_service.eliminar_caja_service(db, caja_id)
    if not eliminada:
        raise HTTPException(status_code=404, detail="Caja no encontrada")
    return None  # 204 No Content

@router.put("/{caja_id}", response_model=CajaOut)
def actualizar_caja(caja_id: int, data: CajaUpdate, db: Session = Depends(get_db)):
    return actualizar_caja_service(db, caja_id, data)

@router.get("/por-fecha/", response_model=CajaOut)
def get_caja_por_fecha(fecha: date = Query(...), db: Session = Depends(get_db)):
    return obtener_caja_con_total_dinamico(db, fecha)