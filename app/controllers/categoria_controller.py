# app/controllers/categoria_controller.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import SessionLocal
from app.schemas.categoria_schema import CategoriaCreate, CategoriaOut
from app.services import categoria_service
from app.schemas.categoria_schema import CategoriaUpdate

router = APIRouter(prefix="/categorias", tags=["Categorias"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("", response_model=CategoriaOut)
def crear_categoria(categoria: CategoriaCreate, db: Session = Depends(get_db)):
    return categoria_service.crear_categoria(db, categoria)

@router.get("", response_model=list[CategoriaOut])
def listar_categorias(db: Session = Depends(get_db)):
    return categoria_service.listar_categorias(db)

@router.delete("/{categoria_id}", status_code=204)
def eliminar_categoria(categoria_id: int, db: Session = Depends(get_db)):
    eliminada = categoria_service.eliminar_categoria(db, categoria_id)
    if not eliminada:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return None  # 204 No Content

@router.put("/{categoria_id}", response_model=CategoriaOut)
def actualizar_categoria(categoria_id: int, data: CategoriaUpdate, db: Session = Depends(get_db)):
    return categoria_service.actualizar_categoria_service(db, categoria_id, data)
