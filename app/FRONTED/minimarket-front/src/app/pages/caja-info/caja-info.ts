import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { CajaService, Caja } from '../../services/caja';
import { ChangeDetectorRef } from '@angular/core';

@Component({
  selector: 'app-caja-info',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './caja-info.html',
  styleUrls: ['./caja-info.scss']
})
export class CajaInfo {
  fechaSeleccionada: string = new Date().toISOString().slice(0, 10);
  caja: Caja | null = null;
  error: string = '';
  loading: boolean = false;

  constructor(private cajaService: CajaService, private cd: ChangeDetectorRef) {}

  buscarCaja() {
    if (this.loading) return;

    this.loading = true;
    this.caja = null;
    this.error = '';

    this.cajaService.obtenerCajaPorFecha(this.fechaSeleccionada).subscribe({
      next: (caja) => {
        this.caja = { ...caja };
        this.loading = false;
        this.cd.detectChanges();  // Forzar actualización de la vista
      },
      error: (err) => {
        this.error = 'Caja no disponible para esa fecha';
        this.loading = false;
        this.cd.detectChanges();
      }
    });
  }
}