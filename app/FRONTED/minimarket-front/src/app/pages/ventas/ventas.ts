import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { AuthService } from '../../services/auth';
import { ChangeDetectorRef } from '@angular/core';

@Component({
  selector: 'app-ventas',
  standalone: true,
  imports: [CommonModule, HttpClientModule],
  templateUrl: './ventas.html',
  styleUrls: ['./ventas.scss']
})
export class Ventas {
  ventaCreada: any = null;
  backendUrl = 'http://localhost:8000/ventas/';
  mensaje: string = '';

  constructor(
    private http: HttpClient,
    private auth: AuthService,
    private cd: ChangeDetectorRef
  ) {}

  generarVenta() {
    // Validar si ya existe una venta activa
    if (this.ventaCreada) {
      this.mensaje = '¡Ya tienes una venta activa!';
      setTimeout(() => this.mensaje = '', 3000);
      return;
    }

    const clienteId = this.auth.currentUser?.uid || "anonimo";
    const ventaData = { cliente_id: clienteId, total: 0, detalles: [] };

    this.http.post(this.backendUrl, ventaData).subscribe({
      next: (data) => {
        this.ventaCreada = data;
        this.mensaje = '¡Se ha generado una venta activa!';
        this.cd.detectChanges(); // Forzar actualización de la vista
        setTimeout(() => this.mensaje = '', 3000);
      },
      error: (err) => console.error('Error al crear venta:', err)
    });
  }

  limpiarVenta() {
    this.ventaCreada = null;
    this.mensaje = 'La venta actual ha sido finalizada.';
    setTimeout(() => this.mensaje = '', 3000);
  }
}
