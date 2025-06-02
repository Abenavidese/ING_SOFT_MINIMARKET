from sqlalchemy import Column, Integer, Float, ForeignKey, Date
from app.config.database import Base

class Venta(Base):
    __tablename__ = "ventas"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    fecha = Column(Date)
    total = Column(Float)
