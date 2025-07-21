from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import SessionLocal
from app.schemas.cliente_schema import ClienteCreate, ClienteOut, ClienteUpdate
from app.services.cliente_service import (
    crear_cliente_service,
    listar_clientes_service,
    eliminar_cliente_service,
    actualizar_cliente_service
)

router = APIRouter(prefix="/clientes", tags=["Clientes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ClienteOut)
def crear_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    return crear_cliente_service(cliente, db)

@router.get("/", response_model=list[ClienteOut])
def listar_clientes(db: Session = Depends(get_db)):
    return listar_clientes_service(db)

@router.delete("/{cliente_id}", status_code=204)
def eliminar_cliente(cliente_id: str, db: Session = Depends(get_db)):
    eliminado = eliminar_cliente_service(cliente_id, db)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return None  # 204 No Content

@router.put("/{cliente_id}", response_model=ClienteOut)
def actualizar_cliente(cliente_id: str, data: ClienteUpdate, db: Session = Depends(get_db)):
    return actualizar_cliente_service(db, cliente_id, data)
