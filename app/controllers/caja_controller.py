from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import SessionLocal
from app.models.caja import Caja
from app.schemas.caja_schema import CajaCreate, CajaOut

router = APIRouter(prefix="/cajas", tags=["Cajas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=CajaOut)
def abrir_caja(caja: CajaCreate, db: Session = Depends(get_db)):
    nueva_caja = Caja(**caja.dict())
    db.add(nueva_caja)
    db.commit()
    db.refresh(nueva_caja)
    return nueva_caja

@router.get("/", response_model=list[CajaOut])
def listar_cajas(db: Session = Depends(get_db)):
    return db.query(Caja).all()
