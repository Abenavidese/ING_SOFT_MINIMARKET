from pydantic import BaseModel
from typing import Optional

class ClienteCreate(BaseModel):
    id: str  # UID de Firebase
    nombre: str
    email: str
    telefono: str
    frecuente: bool = False  # ahora acepta frecuente

class ClienteOut(ClienteCreate):
    id: str  # Ahora el ID también es string (UID de Firebase)

    class Config:
        from_attributes = True  # Correcto

class ClienteUpdate(BaseModel):
    nombre: Optional[str] = None
    email: Optional[str] = None
    telefono: Optional[str] = None
    frecuente: Optional[bool] = None  # Opcional para PUT parcial

    class Config:
        from_attributes = True
