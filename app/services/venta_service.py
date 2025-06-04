from sqlalchemy.orm import Session
from app.models.venta import Venta
from app.schemas.venta_schema import VentaCreate
from app.repositories.venta_repository import crear_venta, obtener_ventas, eliminar_venta
from app.schemas.venta_schema import VentaUpdate
from app.models.venta import Venta
from app.repositories.venta_repository import actualizar_venta



def registrar_venta_service(venta_data: VentaCreate, db: Session) -> Venta:
    nueva_venta = Venta(cliente_id=venta_data.cliente_id, total=venta_data.total)
    return crear_venta(db, nueva_venta)

def listar_ventas_service(db: Session):
    return obtener_ventas(db)

def eliminar_venta_service(venta_id: int, db: Session) -> bool:
    return eliminar_venta(db, venta_id)

def actualizar_venta_service(db: Session, venta_id: int, data: VentaUpdate) -> Venta:
    venta_actualizada = actualizar_venta(db, venta_id, data.dict(exclude_unset=True))
    if not venta_actualizada:
        raise HTTPException(status_code=404, detail="Venta no encontrada")
    return venta_actualizada
