from sqlalchemy.orm import Session
from app.repositories import producto_repository
from app.models.producto import Producto
from app.schemas.producto_schema import ProductoCreate
from app.schemas.producto_schema import ProductoUpdate

def crear_producto_service(db: Session, producto: ProductoCreate):
    return producto_repository.crear_producto(db, producto.dict())

def listar_productos_service(db: Session):
    return producto_repository.listar_productos(db)

def eliminar_producto_service(db: Session, producto_id: int) -> bool:
    return producto_repository.eliminar_producto(db, producto_id)

def actualizar_producto_service(db: Session, producto_id: int, data: ProductoUpdate) -> Producto:
    producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    for key, value in data.model_dump().items():
        setattr(producto, key, value)

    db.commit()
    db.refresh(producto)
    return producto
