import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from '../../services/auth';

@Component({
  selector: 'app-perfil',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './perfil.html',
  styleUrls: ['./perfil.scss']
})
export class Perfil implements OnInit {
  userName: string | null = null;
  userTelefono: string | null = null;
  userEmail: string | null = null;
  userUid: string | null = null;

  editMode: boolean = false; // NUEVO: Controla si los campos son editables

  constructor(private auth: AuthService, private router: Router) {}

  ngOnInit() {
    const currentUser = this.auth.currentUser;
    if (currentUser) {
      const parts = currentUser.displayName?.split('|') || [];
      this.userName = parts[0]?.trim() || 'Sin nombre';
      this.userTelefono = parts[1]?.trim() || 'Sin teléfono';
      this.userEmail = currentUser.email;
      this.userUid = currentUser.uid;
    }
  }

  toggleEdit() {
    this.editMode = !this.editMode;
  }

  async guardarCambios() {
    const displayName = `${this.userName} | ${this.userTelefono}`;
    await this.auth.updateUserProfile(displayName);
    this.editMode = false; // Desactivar edición tras guardar
    alert('Datos actualizados correctamente');
  }
}
