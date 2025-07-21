from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel
from .detalle_venta_schema import DetalleVentaOut

class VentaCreate(BaseModel):
    cliente_id: str  # Cambiado a string para UID Firebase
    total: float

class VentaOut(VentaCreate):
    id: int
    detalles: List[DetalleVentaOut] = []

    class Config:
        orm_mode = True  # Si usas Pydantic v2, reemplaza con 'from_attributes = True'

class VentaUpdate(BaseModel):
    cliente_id: Optional[str]  # Cambiado a string
    fecha: Optional[datetime]
    total: Optional[float]
