import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Categoria {
  id?: number;  
  nombre: string;

}

@Injectable({
  providedIn: 'root'
})
export class CategoriaService {
  private apiUrl = 'http://127.0.0.1:8000/categorias';

  constructor(private http: HttpClient) {}

  listar(): Observable<Categoria[]> {
    return this.http.get<Categoria[]>(this.apiUrl);
  }

  crear(data: Categoria): Observable<Categoria> {
    return this.http.post<Categoria>(this.apiUrl, data);
  }

  actualizar(id: number, data: Categoria): Observable<Categoria> {
    return this.http.put<Categoria>(`${this.apiUrl}/${id}`, data);
  }

  eliminar(id: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}/${id}`);
  }
}
