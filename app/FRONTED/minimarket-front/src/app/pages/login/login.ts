import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from '../../services/auth';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './login.html',
  styleUrls: ['./login.scss']
})
export class LoginComponent {
  nombre = '';
  email = '';
  password = '';
  telefono = '';
  errorMessage = '';
  isRegisterMode = false;

  constructor(private auth: AuthService, private router: Router) {}

  toggleMode() {
    this.isRegisterMode = !this.isRegisterMode;
    this.errorMessage = '';
  }

  async onLogin(event: Event) {
    event.preventDefault();
    if (!this.validateInputs(false)) return;
    try {
      await this.auth.login(this.email, this.password);
      this.errorMessage = '';
      this.router.navigate(['/home']);
    } catch (error: any) {
      console.error('Error Firebase (Login):', error);
      this.errorMessage = this.getFirebaseError(error.code || 'desconocido');
    }
  }

  async onRegisterForm(event: Event) {
    event.preventDefault();
    if (!this.validateInputs(true)) return;
    try {
      await this.auth.register(this.nombre, this.telefono, this.email, this.password);
      this.errorMessage = '';
      alert(`Usuario "${this.nombre}" registrado con éxito`);
      this.router.navigate(['/home']);
    } catch (error: any) {
      console.error('Error Firebase (Register):', error);
      this.errorMessage = this.getFirebaseError(error.code || 'desconocido');
    }
  }

  validateInputs(isRegister: boolean): boolean {
    if (isRegister && this.nombre.trim().length < 2) {
      this.errorMessage = 'El nombre debe tener al menos 2 caracteres.';
      return false;
    }
    if (isRegister && this.telefono.trim().length < 7) {
      this.errorMessage = 'El teléfono debe tener al menos 7 dígitos.';
      return false;
    }
    if (!this.email.includes('@')) {
      this.errorMessage = 'El email no es válido.';
      return false;
    }
    if (this.password.length < 6) {
      this.errorMessage = 'La contraseña debe tener al menos 6 caracteres.';
      return false;
    }
    return true;
  }

  getFirebaseError(code: string): string {
    switch (code) {
      case 'auth/email-already-in-use':
        return 'El correo ya está registrado.';
      case 'auth/invalid-email':
        return 'El formato del correo no es válido.';
      case 'auth/weak-password':
        return 'La contraseña es demasiado débil (mínimo 6 caracteres).';
      case 'auth/user-not-found':
        return 'No existe un usuario con este correo.';
      case 'auth/wrong-password':
        return 'La contraseña es incorrecta.';
      default:
        return 'Error inesperado: ' + code;
    }
  }
}
