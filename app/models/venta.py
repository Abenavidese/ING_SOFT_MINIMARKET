from sqlalchemy import Column, Integer, Float, String, Date
from sqlalchemy.orm import relationship
from app.config.database import Base

class Venta(Base):
    __tablename__ = "ventas"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(String, index=True)  # Ahora es un String para UID Firebase
    fecha = Column(Date)
    total = Column(Float, default=0.0)
    detalles = relationship("DetalleVenta", back_populates="venta")
