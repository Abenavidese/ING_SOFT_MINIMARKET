from sqlalchemy.orm import Session
from app.models.proveedor import Proveedor
from app.schemas.proveedor_schema import ProveedorCreate
from app.repositories import proveedor_repository

def crear_proveedor_service(db: Session, data: ProveedorCreate) -> Proveedor:
    nuevo = Proveedor(**data.model_dump())
    return proveedor_repository.crear_proveedor(db, nuevo)

def listar_proveedores_service(db: Session):
    return proveedor_repository.listar_proveedores(db)

def eliminar_proveedor_service(db: Session, proveedor_id: int) -> bool:
    return proveedor_repository.eliminar_proveedor(db, proveedor_id)
