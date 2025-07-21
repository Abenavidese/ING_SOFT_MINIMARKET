import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AuthService } from '../../services/auth';
import { Router } from '@angular/router';

@Component({
  selector: 'app-menu',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './menu.html',
  styleUrls: ['./menu.scss']
})
export class Menu {
  menuOpen = false;

  constructor(private auth: AuthService, private router: Router) {}

  toggleMenu() {
    this.menuOpen = !this.menuOpen;
  }

  goToProducts() {
    this.router.navigate(['/products']);  // Redirige a la ruta /products
    this.menuOpen = false;                // Cierra el menú
  }

  goToPerfil() {
    this.router.navigate(['/perfil']);  
    this.menuOpen = false;     
  }

  goToVentas() {
  this.router.navigate(['/ventas']);  
  this.menuOpen = false;     
  }

  goToProviders() {
    this.router.navigate(['/providers']);
    this.menuOpen = false;
  }

  goToCategories() {
    this.router.navigate(['/categories']);
    this.menuOpen = false;
  }

  async logout() {
    await this.auth.logout();
    this.router.navigate(['/login']);
  }
}
