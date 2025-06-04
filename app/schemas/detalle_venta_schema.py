from pydantic import BaseModel
from typing import Optional

class DetalleVentaCreate(BaseModel):
    venta_id: int
    producto_id: int
    cantidad: int
    precio_unitario: float

class DetalleVentaUpdate(BaseModel):
    venta_id: Optional[int] = None
    producto_id: Optional[int] = None
    cantidad: Optional[int] = None
    precio_unitario: Optional[float] = None

class DetalleVentaOut(DetalleVentaCreate):
    id: int

    class Config:
        orm_mode = True
