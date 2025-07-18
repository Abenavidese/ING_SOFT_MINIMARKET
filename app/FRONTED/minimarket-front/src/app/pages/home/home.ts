import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { AuthService } from '../../services/auth';
import { Menu } from '../menu/menu'; 

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule, Menu], 
  templateUrl: './home.html',
  styleUrls: ['./home.scss']
})
export class HomeComponent {
  constructor(private auth: AuthService, private router: Router) {}

  async logout() {
    await this.auth.logout();
    this.router.navigate(['/login']);
  }
}
