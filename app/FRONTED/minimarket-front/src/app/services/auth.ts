import { Injectable } from '@angular/core';
import { Auth, signInWithEmailAndPassword, createUserWithEmailAndPassword, signOut, updateProfile, User } from '@angular/fire/auth';
import { HttpClient } from '@angular/common/http';
import { firstValueFrom } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private backendUrl = 'http://localhost:8000/clientes/'; // URL de tu API backend

  constructor(private auth: Auth, private http: HttpClient) {}

  get currentUser(): User | null {
    return this.auth.currentUser;
  }

  // Login
  login(email: string, password: string) {
    return signInWithEmailAndPassword(this.auth, email, password);
  }

  // Registro con nombre y teléfono
  async register(nombre: string, telefono: string, email: string, password: string) {
    const userCredential = await createUserWithEmailAndPassword(this.auth, email, password);

    if (userCredential.user) {
      // Actualizamos el perfil
      await updateProfile(userCredential.user, { 
        displayName: `${nombre} | ${telefono}` 
      });

      // Enviamos el UID de Firebase como 'id'
      const cliente = { 
        id: userCredential.user.uid, 
        nombre, 
        email, 
        telefono, 
        frecuente: false 
      };
      await firstValueFrom(this.http.post(this.backendUrl, cliente));
    }

    return userCredential;
  }

  async updateUserProfile(displayName: string) {
    if (this.currentUser) {
      await updateProfile(this.currentUser, { displayName });
    }
  }
  // Logout
  logout() {
    return signOut(this.auth);
  }
}
