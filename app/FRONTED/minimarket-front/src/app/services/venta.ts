import { Injectable } from '@angular/core';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';

export interface DetalleVentaCreate {
  producto_id: number;
  cantidad: number;
}

export interface VentaCreate {
  cliente_id: string;
  fecha: string; // 'YYYY-MM-DD'
  detalles: DetalleVentaCreate[];
}

export interface DetalleVentaOut extends DetalleVentaCreate {
  id: number;
  venta_id: number;
  precio_unitario: number;
}

export interface VentaOut {
  id: number;
  cliente_id: string;
  fecha: string;
  total: number;
  detalles: DetalleVentaOut[];
}

@Injectable({
  providedIn: 'root'
})
export class VentaService {
  private apiUrl = 'http://localhost:8000/ventas'; // Cambia si tu backend está en otro puerto o ruta

  constructor(private http: HttpClient) {}

  // Crear nueva venta
  crearVenta(venta: VentaCreate): Observable<VentaOut> {
    return this.http.post<VentaOut>(this.apiUrl, venta).pipe(
      catchError(this.manejarError)
    );
  }

  // Listar ventas, opcional filtro por cliente_id
  listarVentas(clienteId?: string): Observable<VentaOut[]> {
    let url = this.apiUrl;
    if (clienteId) {
      url += `?cliente_id=${clienteId}`;
    }
    return this.http.get<VentaOut[]>(url).pipe(
      catchError(this.manejarError)
    );
  }

  // Manejo básico de errores HTTP
  private manejarError(error: HttpErrorResponse) {
    // Aquí podrías hacer más lógica según error.status o error.error
    console.error('Error en venta.service:', error);
    return throwError(() => new Error('Error en la comunicación con el backend'));
  }
}