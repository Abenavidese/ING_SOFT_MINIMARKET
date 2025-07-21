from sqlalchemy import Column, String, Boolean
from app.config.database import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(String, primary_key=True, index=True)  # UID de Firebase como ID
    nombre = Column(String, nullable=False)
    email = Column(String, nullable=False)
    telefono = Column(String, nullable=False)
    frecuente = Column(Boolean, default=False)
