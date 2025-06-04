# app/services/categoria_service.py

from sqlalchemy.orm import Session
from app.schemas.categoria_schema import CategoriaCreate
from app.models.categoria import Categoria
from app.repositories import categoria_repository

def crear_categoria(db: Session, categoria: CategoriaCreate) -> Categoria:
    return categoria_repository.crear_categoria(db, categoria)

def listar_categorias(db: Session) -> list[Categoria]:
    return categoria_repository.listar_categorias(db)

def eliminar_categoria(db: Session, categoria_id: int) -> bool:
    return categoria_repository.eliminar_categoria(db, categoria_id)
