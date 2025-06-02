from sqlalchemy import Column, Integer, String, Boolean
from app.config.database import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    correo = Column(String)
    frecuente = Column(Boolean, default=False)
