from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.config.database import Base

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    precio = Column(Float)
    stock = Column(Integer)
    proveedor_id = Column(Integer, ForeignKey("proveedores.id"))
    categoria_id = Column(Integer, ForeignKey("categorias.id"))
