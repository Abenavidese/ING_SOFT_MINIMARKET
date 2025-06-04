from pydantic import BaseModel
from datetime import date

class CajaCreate(BaseModel):
    fecha: date
    estado: str
    total_dia: float

class CajaOut(CajaCreate):
    id: int

    class Config:
        orm_mode = True
