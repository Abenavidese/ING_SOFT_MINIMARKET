from pydantic import BaseModel
from typing import Optional

class ProveedorCreate(BaseModel):
    nombre: str
    contacto: str

class ProveedorUpdate(BaseModel):
    nombre: Optional[str]
    contacto: Optional[str]

class ProveedorOut(ProveedorCreate):
    id: int

    class Config:
        orm_mode = True
