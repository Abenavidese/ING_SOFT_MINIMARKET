from sqlalchemy.orm import Session
from app.models.venta import Venta
from app.schemas.venta_schema import VentaCreate
from app.repositories.venta_repository import crear_venta, obtener_ventas

def registrar_venta_service(venta_data: VentaCreate, db: Session) -> Venta:
    nueva_venta = Venta(cliente_id=venta_data.cliente_id, total=venta_data.total)
    return crear_venta(db, nueva_venta)

def listar_ventas_service(db: Session):
    return obtener_ventas(db)
