from typing import List
from pydantic import BaseModel
from .detalle_venta_schema import DetalleVentaOut

class VentaCreate(BaseModel):
    cliente_id: int
    total: float

class VentaOut(VentaCreate):
    id: int
    detalles: List[DetalleVentaOut] = []

    class Config:
        orm_mode = True
