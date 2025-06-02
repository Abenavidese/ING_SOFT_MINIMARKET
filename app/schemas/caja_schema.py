from pydantic import BaseModel

class CajaCreate(BaseModel):
    monto_inicial: float
    monto_final: float

class CajaOut(CajaCreate):
    id: int

    class Config:
        orm_mode = True
