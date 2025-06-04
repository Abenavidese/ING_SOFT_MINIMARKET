from pydantic import BaseModel

class CategoriaCreate(BaseModel):
    nombre: str

class CategoriaUpdate(BaseModel):
    nombre: str

class CategoriaOut(CategoriaCreate):
    id: int

    class Config:
        orm_mode = True
