import { Component, OnInit } from '@angular/core';
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
    proveedor_id: 1,
    categoria_id: 1
  };

  constructor(
    private productService: ProductService,
    private proveedorService: ProveedorService,
    private categoriaService: CategoriaService
  ) {}

  ngOnInit() {
    this.cargarProductos();
    this.cargarProveedores();
    this.cargarCategorias();
  }

  cargarProductos() {
    this.productService.listar().subscribe({
      next: (data) => (this.productos = data),
      error: (err) => console.error('Error al listar productos:', err)
    });
  }

  cargarProveedores() {
    this.proveedorService.listar().subscribe({
      next: (data) => (this.proveedores = data),
      error: (err) => console.error('Error al listar proveedores:', err)
    });
  }

  cargarCategorias() {
    this.categoriaService.listar().subscribe({
      next: (data) => (this.categorias = data),
      error: (err) => console.error('Error al listar categorías:', err)
    });
  }

  crearProducto() {
    this.productService.crear(this.nuevoProducto).subscribe({
      next: () => {
        this.nuevoProducto = { nombre: '', precio: 0, stock: 0, proveedor_id: 1, categoria_id: 1 };
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
}
