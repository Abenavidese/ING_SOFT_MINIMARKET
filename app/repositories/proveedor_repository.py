from sqlalchemy.orm import Session
from app.models.proveedor import Proveedor
from typing import List

def crear_proveedor(db: Session, proveedor: Proveedor) -> Proveedor:
    db.add(proveedor)
    db.commit()
    db.refresh(proveedor)
    return proveedor

def listar_proveedores(db: Session) -> List[Proveedor]:
    return db.query(Proveedor).all()

def eliminar_proveedor(db: Session, proveedor_id: int) -> bool:
    proveedor = db.query(Proveedor).filter(Proveedor.id == proveedor_id).first()
    if proveedor:
        db.delete(proveedor)
        db.commit()
        return True
    return False
