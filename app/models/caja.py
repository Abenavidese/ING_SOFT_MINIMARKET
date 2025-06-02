from sqlalchemy import Column, Integer, Float, Date, String
from app.config.database import Base

class Caja(Base):
    __tablename__ = "cajas"

    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date)
    estado = Column(String)
    total_dia = Column(Float)
