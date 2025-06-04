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

def eliminar_categoria(db: Session, categoria_id: int) -> bool:
    categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()
    if categoria:
        db.delete(categoria)
        db.commit()
        return True
    return False
