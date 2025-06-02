from pydantic import BaseModel

# Para crear un producto
class ProductoCreate(BaseModel):
    nombre: str
    precio: float
    stock: int
    proveedor_id: int
    categoria_id: int

# Para mostrar un producto 
class ProductoOut(ProductoCreate):
    id: int

    class Config:
        orm_mode = True
