import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { AuthService } from '../../services/auth';

@Component({
  selector: 'app-perfil',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './perfil.html',
  styleUrls: ['./perfil.scss']
})
export class Perfil implements OnInit {
  userName: string | null = null;
  userTelefono: string | null = null;
  userEmail: string | null = null;
  userUid: string | null = null;

  constructor(private auth: AuthService, private router: Router) {}

  ngOnInit() {
    const currentUser = this.auth.currentUser;
    if (currentUser) {
      // Extraer nombre y teléfono del displayName (si están concatenados)
      const parts = currentUser.displayName?.split('|') || [];
      this.userName = parts[0]?.trim() || 'Sin nombre';
      this.userTelefono = parts[1]?.trim() || 'Sin teléfono';
      this.userEmail = currentUser.email;
      this.userUid = currentUser.uid;
    }
  }

  async logout() {
    await this.auth.logout();
    this.router.navigate(['/login']);
  }
}
