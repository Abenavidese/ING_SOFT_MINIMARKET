from pydantic import BaseModel
from typing import Optional

class DetalleVentaCreate(BaseModel):
    producto_id: int
    cantidad: int

class DetalleVentaOut(BaseModel):
    id: int
    venta_id: int
    producto_id: int
    cantidad: int
    precio_unitario: float

    class Config:
        orm_mode = True

class DetalleVentaUpdate(BaseModel):
    producto_id: Optional[int] = None
    cantidad: Optional[int] = None