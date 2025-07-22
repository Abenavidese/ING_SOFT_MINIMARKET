import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Producto, ProductService } from '../../services/product-service';
import { Proveedor, ProveedorService } from '../../services/proveedor-service';
import { Categoria, CategoriaService } from '../../services/categoria-service';

@Component({
  selector: 'app-products',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './products.html',
  styleUrls: ['./products.scss']
})
export class Products implements OnInit {
  productos: Producto[] = [];
  proveedores: Proveedor[] = [];
  categorias: Categoria[] = [];

  nuevoProducto: Producto = {
    nombre: '',
    precio: 0,
    stock: 0,
    proveedor_id: 0,
    categoria_id: 0
  };

  editandoProducto: Producto | null = null; // <-- Guardamos el producto en edición

  constructor(
    private productService: ProductService,
    private proveedorService: ProveedorService,
    private categoriaService: CategoriaService,
    private cdr: ChangeDetectorRef
  ) {}

  ngOnInit() {
    this.cargarProductos();
    this.cargarProveedores();
    this.cargarCategorias();
  }

  cargarProductos() {
    this.productService.listar().subscribe({
      next: (data) => {
        this.productos = data;
        this.cdr.detectChanges();
      },
      error: (err) => console.error('Error al listar productos:', err)
    });
  }

  cargarProveedores() {
    this.proveedorService.listar().subscribe({
      next: (data) => {
        this.proveedores = data;
        if (this.proveedores.length > 0) {
          this.nuevoProducto.proveedor_id = this.proveedores[0].id!;
        }
        this.cdr.detectChanges();
      },
      error: (err) => console.error('Error al listar proveedores:', err)
    });
  }

  cargarCategorias() {
    this.categoriaService.listar().subscribe({
      next: (data) => {
        this.categorias = data;
        if (this.categorias.length > 0) {
          this.nuevoProducto.categoria_id = this.categorias[0].id!;
        }
        this.cdr.detectChanges();
      },
      error: (err) => console.error('Error al listar categorías:', err)
    });
  }

  crearProducto() {
    this.productService.crear(this.nuevoProducto).subscribe({
      next: () => {
        this.nuevoProducto = {
          nombre: '',
          precio: 0,
          stock: 0,
          proveedor_id: this.proveedores.length > 0 ? this.proveedores[0].id! : 0,
          categoria_id: this.categorias.length > 0 ? this.categorias[0].id! : 0
        };
        this.cargarProductos();
      },
      error: (err) => console.error('Error al crear producto:', err)
    });
  }

  eliminarProducto(id: number) {
    this.productService.eliminar(id).subscribe({
      next: () => this.cargarProductos(),
      error: (err) => console.error('Error al eliminar producto:', err)
    });
  }

  // ---- NUEVO ----

  editarProducto(producto: Producto) {
    this.editandoProducto = { ...producto }; // Clonamos el producto a editar
  }

  cancelarEdicion() {
    this.editandoProducto = null;
  }

  actualizarProducto() {
    if (this.editandoProducto && this.editandoProducto.id) {
      this.productService.actualizar(this.editandoProducto.id, this.editandoProducto).subscribe({
        next: () => {
          this.editandoProducto = null;
          this.cargarProductos();
        },
        error: (err) => console.error('Error al actualizar producto:', err)
      });
    }
  }
}
