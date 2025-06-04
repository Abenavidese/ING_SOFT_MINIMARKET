from pydantic import BaseModel

class DetalleVentaCreate(BaseModel):
    venta_id: int
    producto_id: int
    cantidad: int
    precio_unitario: float

class DetalleVentaOut(DetalleVentaCreate):
    id: int

    class Config:
        orm_mode = True
