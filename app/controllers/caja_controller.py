from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import SessionLocal
from app.schemas.caja_schema import CajaCreate, CajaOut
from app.services import caja_service

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
