# app/controllers/categoria_controller.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import SessionLocal
from app.schemas.categoria_schema import CategoriaCreate, CategoriaOut
from app.services import categoria_service

router = APIRouter(prefix="/categorias", tags=["Categorias"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=CategoriaOut)
def crear_categoria(categoria: CategoriaCreate, db: Session = Depends(get_db)):
    return categoria_service.crear_categoria(db, categoria)

@router.get("/", response_model=list[CategoriaOut])
def listar_categorias(db: Session = Depends(get_db)):
    return categoria_service.listar_categorias(db)
