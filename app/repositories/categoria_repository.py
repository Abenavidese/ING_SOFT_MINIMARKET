# app/repositories/categoria_repository.py

from sqlalchemy.orm import Session
from app.models.categoria import Categoria
from app.schemas.categoria_schema import CategoriaCreate

def crear_categoria(db: Session, categoria: CategoriaCreate) -> Categoria:
    nueva = Categoria(**categoria.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

def listar_categorias(db: Session) -> list[Categoria]:
    return db.query(Categoria).all()
