from pydantic import BaseModel

class ClienteCreate(BaseModel):
    nombre: str
    email: str
    telefono: str

class ClienteOut(ClienteCreate):
    id: int

    class Config:
        orm_mode = True
