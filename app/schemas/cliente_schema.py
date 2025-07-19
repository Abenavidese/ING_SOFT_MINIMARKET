from pydantic import BaseModel
from typing import Optional

class ClienteCreate(BaseModel):
    nombre: str
    email: str
    telefono: str
    frecuente: bool = False  # 🚀 ahora acepta frecuente

class ClienteOut(ClienteCreate):
    id: int

    class Config:
        from_attributes = True  # 🚀 ya correcto

class ClienteUpdate(BaseModel):
    nombre: Optional[str] = None
    email: Optional[str] = None
    telefono: Optional[str] = None
    frecuente: Optional[bool] = None  # 🚀 opcional, para PUT parcial

    class Config:
        from_attributes = True