from sqlalchemy.orm import Session
from app.models.venta import Venta
from typing import Optional
from app.models.venta import Venta
from app.models.detalle_venta import DetalleVenta
from app.models.producto import Producto
from fastapi import HTTPException
from datetime import date

def crear_venta_con_detalles(db: Session, cliente_id: str, fecha: date, detalles: list[dict]) -> Venta:
    total_venta = 0.0
    detalles_validos = []

    # Validar stock y calcular total
    for det in detalles:
        producto = db.query(Producto).filter(Producto.id == det["producto_id"]).first()
        if not producto:
            raise HTTPException(status_code=404, detail=f"Producto {det['producto_id']} no encontrado")
        if producto.stock < det["cantidad"]:
            raise HTTPException(status_code=400, detail=f"Stock insuficiente para producto {producto.nombre}")
        subtotal = producto.precio * det["cantidad"]
        total_venta += subtotal
        detalles_validos.append({
            "producto_id": producto.id,
            "cantidad": det["cantidad"],
            "precio_unitario": producto.precio
        })

    # Crear venta
    nueva_venta = Venta(cliente_id=cliente_id, fecha=fecha, total=total_venta)
    db.add(nueva_venta)
    db.flush()  # Para obtener nueva_venta.id sin commit

    # Crear detalles y actualizar stock
    for det in detalles_validos:
        detalle_venta = DetalleVenta(
            venta_id=nueva_venta.id,
            producto_id=det["producto_id"],
            cantidad=det["cantidad"],
            precio_unitario=det["precio_unitario"]
        )
        db.add(detalle_venta)

        producto = db.query(Producto).filter(Producto.id == det["producto_id"]).first()
        producto.stock -= det["cantidad"]

    # Commit final para toda la transacción
    db.commit()
    db.refresh(nueva_venta)
    return nueva_venta

def obtener_ventas(db: Session, cliente_id: Optional[str] = None) -> list[Venta]:
    query = db.query(Venta)
    if cliente_id:
        query = query.filter(Venta.cliente_id == cliente_id)
    return query.all()

def eliminar_venta(db: Session, venta_id: int) -> bool:
    venta = db.query(Venta).filter(Venta.id == venta_id).first()
    if venta:
        db.delete(venta)
        db.commit()
        return True
    return False

def actualizar_venta(db: Session, venta_id: int, data: dict) -> Venta:
    venta = db.query(Venta).filter(Venta.id == venta_id).first()
    if not venta:
        return None
    for key, value in data.items():
        setattr(venta, key, value)
    db.commit()
    db.refresh(venta)
    return venta
