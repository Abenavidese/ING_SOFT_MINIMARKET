from sqlalchemy.orm import Session
from app.models.caja import Caja
from app.schemas.caja_schema import CajaCreate
from app.repositories import caja_repository
from app.schemas.caja_schema import CajaUpdate

def crear_caja_service(db: Session, caja_data: CajaCreate) -> Caja:
    nueva_caja = Caja(**caja_data.model_dump())
    return caja_repository.crear_caja(db, nueva_caja)

def listar_cajas_service(db: Session) -> list[Caja]:
    return caja_repository.obtener_todas_las_cajas(db)

def eliminar_caja_service(db: Session, caja_id: int) -> bool:
    return caja_repository.eliminar_caja(db, caja_id)

def actualizar_caja_service(db: Session, caja_id: int, data: CajaUpdate) -> Caja:
    caja = db.query(Caja).filter(Caja.id == caja_id).first()
    if not caja:
        raise HTTPException(status_code=404, detail="Caja no encontrada")

    for key, value in data.model_dump().items():
        setattr(caja, key, value)

    db.commit()
    db.refresh(caja)
    return caja
