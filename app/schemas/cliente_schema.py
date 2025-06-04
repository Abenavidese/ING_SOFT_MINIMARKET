from pydantic import BaseModel

class ClienteCreate(BaseModel):
    nombre: str
    email: str
    telefono: str

class ClienteOut(ClienteCreate):
    id: int
    frecuente: bool 

    class Config:
        orm_mode = True

class ClienteUpdate(BaseModel):
    nombre: str
    email: str
    telefono: str
    frecuente: bool

    class Config:
        from_attributes = True
