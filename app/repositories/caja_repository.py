from sqlalchemy.orm import Session
from app.models.caja import Caja

def crear_caja(db: Session, caja: Caja) -> Caja:
    db.add(caja)
    db.commit()
    db.refresh(caja)
    return caja

def obtener_todas_las_cajas(db: Session) -> list[Caja]:
    return db.query(Caja).all()

def eliminar_caja(db: Session, caja_id: int) -> bool:
    caja = db.query(Caja).filter(Caja.id == caja_id).first()
    if caja:
        db.delete(caja)
        db.commit()
        return True
    return False
