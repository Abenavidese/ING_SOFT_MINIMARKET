from sqlalchemy.orm import Session
from app.repositories import producto_repository
from app.schemas.producto_schema import ProductoCreate

def crear_producto_service(db: Session, producto: ProductoCreate):
    return producto_repository.crear_producto(db, producto.dict())

def listar_productos_service(db: Session):
    return producto_repository.listar_productos(db)

def eliminar_producto_service(db: Session, producto_id: int) -> bool:
    return producto_repository.eliminar_producto(db, producto_id)
