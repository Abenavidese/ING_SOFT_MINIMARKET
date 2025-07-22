import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Caja {
  id: number;
  fecha: string;
  estado: string;
  total_dia: number;
}

@Injectable({
  providedIn: 'root'
})
export class CajaService {
  private apiUrl = 'http://localhost:8000/cajas';

  constructor(private http: HttpClient) {}

  obtenerCajaPorFecha(fecha: string): Observable<Caja> {
    return this.http.get<Caja>(`${this.apiUrl}/por-fecha/?fecha=${fecha}`);
  }
}
