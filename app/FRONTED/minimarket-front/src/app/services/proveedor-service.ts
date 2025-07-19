import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Proveedor {
  id?: number;       // Lo asigna el backend
  nombre: string;
  contacto: string;
}

@Injectable({
  providedIn: 'root'
})
export class ProveedorService {
  private apiUrl = 'http://127.0.0.1:8000/proveedores'; // Ajusta tu backend

  constructor(private http: HttpClient) {}

  listar(): Observable<Proveedor[]> {
    return this.http.get<Proveedor[]>(this.apiUrl);  // <--- Sin la barra final
  }
  
  actualizar(id: number, data: Proveedor): Observable<Proveedor> {
  return this.http.put<Proveedor>(`${this.apiUrl}/${id}`, data);
}

  crear(data: Proveedor): Observable<Proveedor> {
    return this.http.post<Proveedor>(this.apiUrl, data);
  }

  eliminar(id: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}/${id}`);
  }
}
