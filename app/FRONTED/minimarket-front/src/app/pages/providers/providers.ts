import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ProveedorService, Proveedor } from '../../services/proveedor-service';

@Component({
  selector: 'app-providers',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './providers.html',
  styleUrls: ['./providers.scss']
})
export class Providers implements OnInit {
  proveedores: Proveedor[] = [];
  nuevoProveedor: Proveedor = { nombre: '', contacto: '' };

  // Variables para edición
  editando: boolean = false;
  proveedorEditando: Proveedor = { id: 0, nombre: '', contacto: '' };

  constructor(
    private proveedorService: ProveedorService,
    private cdr: ChangeDetectorRef // <-- Se inyecta el ChangeDetectorRef
  ) {}

  ngOnInit() {
    this.cargarProveedores();
  }

  cargarProveedores() {
    this.proveedorService.listar().subscribe({
      next: (data) => {
        this.proveedores = data;
        this.cdr.detectChanges(); // <-- Fuerza la actualización de la vista
      },
      error: (err) => console.error('Error al listar proveedores:', err)
    });
  }

  crearProveedor() {
    this.proveedorService.crear(this.nuevoProveedor).subscribe({
      next: () => {
        this.nuevoProveedor = { nombre: '', contacto: '' };
        this.cargarProveedores();
      },
      error: (err) => console.error('Error al crear proveedor:', err)
    });
  }

  editarProveedor(proveedor: Proveedor) {
    this.editando = true;
    this.proveedorEditando = { ...proveedor }; // Copiamos el proveedor a editar
  }

  guardarEdicion() {
    if (!this.proveedorEditando.id) return;

    this.proveedorService.actualizar(this.proveedorEditando.id!, this.proveedorEditando).subscribe({
      next: () => {
        this.editando = false;
        this.proveedorEditando = { id: 0, nombre: '', contacto: '' };
        this.cargarProveedores();
      },
      error: (err) => console.error('Error al actualizar proveedor:', err)
    });
  }

  cancelarEdicion() {
    this.editando = false;
    this.proveedorEditando = { id: 0, nombre: '', contacto: '' };
  }

  eliminarProveedor(id: number) {
    this.proveedorService.eliminar(id).subscribe({
      next: () => this.cargarProveedores(),
      error: (err) => console.error('Error al eliminar proveedor:', err)
    });
  }
}
