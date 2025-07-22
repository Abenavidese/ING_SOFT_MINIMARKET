from typing import List, Optional
from datetime import date
from pydantic import BaseModel
from .detalle_venta_schema import DetalleVentaOut, DetalleVentaCreate

class VentaCreate(BaseModel):
    cliente_id: str           # O int, según como manejes cliente
    fecha: date
    detalles: List[DetalleVentaCreate]

class VentaOut(BaseModel):
    id: int
    cliente_id: str
    fecha: date
    total: float
    detalles: List[DetalleVentaOut] = []

    class Config:
        orm_mode = True  # o from_attributes=True

class VentaUpdate(BaseModel):
    cliente_id: Optional[str] = None
    fecha: Optional[date] = None
