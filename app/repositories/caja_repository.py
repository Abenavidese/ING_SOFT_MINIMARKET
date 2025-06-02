from sqlalchemy.orm import Session
from app.models.caja import Caja

def crear_caja(db: Session, caja: Caja) -> Caja:
    db.add(caja)
    db.commit()
    db.refresh(caja)
    return caja

def obtener_todas_las_cajas(db: Session) -> list[Caja]:
    return db.query(Caja).all()
