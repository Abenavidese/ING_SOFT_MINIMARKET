from pydantic import BaseModel

class DetalleVentaCreate(BaseModel):
    venta_id: int
    producto_id: int
    cantidad: int
    subtotal: float

class DetalleVentaOut(DetalleVentaCreate):
    id: int

    class Config:
        orm_mode = True
