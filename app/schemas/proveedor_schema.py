from pydantic import BaseModel

class ProveedorCreate(BaseModel):
    nombre: str
    contacto: str

class ProveedorOut(ProveedorCreate):
    id: int

    class Config:
        orm_mode = True
