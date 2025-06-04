from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel
from .detalle_venta_schema import DetalleVentaOut

class VentaCreate(BaseModel):
    cliente_id: int
    total: float

class VentaOut(VentaCreate):
    id: int
    detalles: List[DetalleVentaOut] = []

    class Config:
        orm_mode = True  # Si estás en Pydantic v2, cámbialo por 'from_attributes = True'

class VentaUpdate(BaseModel):
    cliente_id: Optional[int]
    fecha: Optional[datetime]
    total: Optional[float]
