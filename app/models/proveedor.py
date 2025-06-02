from sqlalchemy import Column, Integer, String
from app.config.database import Base

class Proveedor(Base):
    __tablename__ = "proveedores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    contacto = Column(String)
    direccion = Column(String)
