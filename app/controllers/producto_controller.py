from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import SessionLocal
from app.schemas.producto_schema import ProductoCreate, ProductoOut
from app.services import producto_service
from app.schemas.producto_schema import ProductoUpdate, ProductoOut
from app.services.producto_service import actualizar_producto_service

router = APIRouter(prefix="/productos", tags=["Productos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ProductoOut)
def crear_producto(producto: ProductoCreate, db: Session = Depends(get_db)):
    return producto_service.crear_producto_service(db, producto)

@router.get("/", response_model=list[ProductoOut])
def listar_productos(db: Session = Depends(get_db)):
    return producto_service.listar_productos_service(db)

@router.delete("/{producto_id}", status_code=204)
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    eliminado = producto_service.eliminar_producto_service(db, producto_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return None  # 204 No Content

@router.put("/{producto_id}", response_model=ProductoOut)
def actualizar_producto(producto_id: int, data: ProductoUpdate, db: Session = Depends(get_db)):
    return actualizar_producto_service(db, producto_id, data)
