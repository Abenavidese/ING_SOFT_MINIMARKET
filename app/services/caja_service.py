from sqlalchemy.orm import Session
from app.models.caja import Caja
from app.schemas.caja_schema import CajaCreate
from app.repositories import caja_repository

def crear_caja_service(db: Session, caja_data: CajaCreate) -> Caja:
    nueva_caja = Caja(**caja_data.model_dump())
    return caja_repository.crear_caja(db, nueva_caja)

def listar_cajas_service(db: Session) -> list[Caja]:
    return caja_repository.obtener_todas_las_cajas(db)
