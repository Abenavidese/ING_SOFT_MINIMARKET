import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { AuthService } from '../../services/auth';
import { ProductService, Producto } from '../../services/product-service';
import { VentaService, VentaCreate, VentaOut } from '../../services/venta';

@Component({
  selector: 'app-ventas',
  standalone: true,
  imports: [CommonModule, HttpClientModule],
  templateUrl: './ventas.html',
  styleUrls: ['./ventas.scss'],
})
export class Ventas implements OnInit {
  productos: Producto[] = [];
  productosSeleccionados: Array<{ producto: Producto; cantidad: number }> = [];
  clienteId: string = '';
  fechaVenta: string = new Date().toISOString().slice(0, 10); // YYYY-MM-DD
  subtotal: number = 0;
  total: number = 0;
  mensaje: string = '';
  ventaCreada: VentaOut | null = null;

  constructor(
    private http: HttpClient,
    private auth: AuthService,
    private cd: ChangeDetectorRef,
    private productService: ProductService,
    private ventaService: VentaService
  ) {}

  cargarProductos() {
    this.productService.listar().subscribe({
      next: (productos) => {
        // Filtra productos con stock mayor que cero
        this.productos = productos.filter(p => p.stock > 0);
        this.cd.detectChanges(); // (opcional) fuerza actualización
      },
      error: (error) => {
        console.error('Error al cargar productos', error);
        this.mensaje = 'Error al cargar productos';
      },
    });
  }

  ngOnInit() {
    this.clienteId = this.auth.currentUser?.uid || 'anonimo';
    this.cargarProductos();
  }

  isProductoSeleccionado(productoId: number): boolean {
    return this.productosSeleccionados.some(ps => ps.producto.id === productoId);
  }

  agregarProducto(producto: Producto) {
    if (!this.isProductoSeleccionado(producto.id!)) {
      this.productosSeleccionados.push({ producto, cantidad: 1 });
      this.calcularTotal();
    }
  }

  quitarProducto(productoId: number) {
    this.productosSeleccionados = this.productosSeleccionados.filter(p => p.producto.id !== productoId);
    this.calcularTotal();
  }

  cambiarCantidad(productoId: number, cantidad: number) {
    const p = this.productosSeleccionados.find(p => p.producto.id === productoId);
    if (p) {
      if (cantidad > 0 && cantidad <= p.producto.stock) {
        p.cantidad = cantidad;
        this.calcularTotal();
      } else {
        this.mensaje = 'Cantidad inválida o supera el stock';
        setTimeout(() => (this.mensaje = ''), 3000);
      }
    }
  }

  calcularTotal() {
    this.subtotal = this.productosSeleccionados.reduce((acc, p) => acc + p.producto.precio * p.cantidad, 0);
    this.total = this.subtotal; // Puedes agregar impuestos si quieres
  }

  generarVenta() {
    if (this.productosSeleccionados.length === 0) {
      this.mensaje = 'Selecciona al menos un producto';
      setTimeout(() => (this.mensaje = ''), 3000);
      return;
    }

    const ventaData: VentaCreate = {
      cliente_id: this.clienteId,
      fecha: this.fechaVenta,
      detalles: this.productosSeleccionados.map(p => ({
        producto_id: p.producto.id!,
        cantidad: p.cantidad,
      })),
    };

    this.ventaService.crearVenta(ventaData).subscribe({
      next: (ventaCreada) => {
        this.ventaCreada = ventaCreada;
        this.mensaje = `Venta creada con ID: ${ventaCreada.id} y total: ${ventaCreada.total}`;
        this.productosSeleccionados = [];
        this.calcularTotal();

        this.cargarProductos();

        this.cd.detectChanges();
        setTimeout(() => (this.mensaje = ''), 5000);
      },
      error: (err) => {
        this.mensaje = 'Error al crear la venta: ' + err.message;
        setTimeout(() => (this.mensaje = ''), 5000);
      },
    });
  }

  limpiarVenta() {
    this.ventaCreada = null;
    this.mensaje = 'La venta actual ha sido finalizada.';
    setTimeout(() => (this.mensaje = ''), 3000);
  }
}
