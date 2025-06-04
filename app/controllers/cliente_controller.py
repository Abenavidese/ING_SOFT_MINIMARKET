from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import SessionLocal
from app.schemas.cliente_schema import ClienteCreate, ClienteOut

router = APIRouter(prefix="/clientes", tags=["Clientes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ClienteOut)
def crear_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    nuevo_cliente = Cliente(**cliente.dict())
    db.add(nuevo_cliente)
    db.commit()
    db.refresh(nuevo_cliente)
    return nuevo_cliente

@router.get("/", response_model=list[ClienteOut])
def listar_clientes(db: Session = Depends(get_db)):
    return db.query(Cliente).all()
