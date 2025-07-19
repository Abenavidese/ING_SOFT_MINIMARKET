import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { CategoriaService, Categoria } from '../../services/categoria-service';
import { ChangeDetectorRef } from '@angular/core';
@Component({
  selector: 'app-categories',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './categories.html',
  styleUrls: ['./categories.scss']
})
export class Categories implements OnInit {
  categorias: Categoria[] = [];
  nuevaCategoria: Categoria = { nombre: '' };

  editando = false;
  categoriaEditando: Categoria = { id: 0, nombre: '' };

  constructor(private categoriaService: CategoriaService, private cdr: ChangeDetectorRef) {}

  ngOnInit() {
    // Cargar categorías automáticamente al entrar en la página
    this.cargarCategorias();
  }

  cargarCategorias() {
    this.categoriaService.listar().subscribe({
      next: (data) => {
        this.categorias = data;
        this.cdr.detectChanges(); // Asegura que los cambios se reflejen en la vista
        console.log('Categorías cargadas:', this.categorias);
      },
      error: (err) => console.error('Error al listar categorías:', err)
    });
  }

  crearCategoria() {
    this.categoriaService.crear(this.nuevaCategoria).subscribe({
      next: () => {
        this.nuevaCategoria = { nombre: '' };
        this.cargarCategorias();
      },
      error: (err) => console.error('Error al crear categoría:', err)
    });
  }

  editarCategoria(categoria: Categoria) {
    this.editando = true;
    this.categoriaEditando = { ...categoria };
  }

  guardarEdicion() {
    if (!this.categoriaEditando.id) return;
    this.categoriaService.actualizar(this.categoriaEditando.id!, this.categoriaEditando).subscribe({
      next: () => {
        this.editando = false;
        this.categoriaEditando = { id: 0, nombre: '' };
        this.cargarCategorias();
      },
      error: (err) => console.error('Error al actualizar categoría:', err)
    });
  }

  cancelarEdicion() {
    this.editando = false;
    this.categoriaEditando = { id: 0, nombre: '' };
  }

  eliminarCategoria(id: number) {
    this.categoriaService.eliminar(id).subscribe({
      next: () => this.cargarCategorias(),
      error: (err) => console.error('Error al eliminar categoría:', err)
    });
  }
}
