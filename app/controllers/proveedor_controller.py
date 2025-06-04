from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import SessionLocal
from app.schemas.proveedor_schema import ProveedorCreate, ProveedorOut
from app.services import proveedor_service

router = APIRouter(prefix="/proveedores", tags=["Proveedores"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ProveedorOut)
def crear_proveedor(proveedor: ProveedorCreate, db: Session = Depends(get_db)):
    return proveedor_service.crear_proveedor_service(db, proveedor)

@router.get("/", response_model=list[ProveedorOut])
def listar_proveedores(db: Session = Depends(get_db)):
    return proveedor_service.listar_proveedores_service(db)

@router.delete("/{proveedor_id}", status_code=204)
def eliminar_proveedor(proveedor_id: int, db: Session = Depends(get_db)):
    eliminado = proveedor_service.eliminar_proveedor_service(db, proveedor_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Proveedor no encontrado")
    return None
