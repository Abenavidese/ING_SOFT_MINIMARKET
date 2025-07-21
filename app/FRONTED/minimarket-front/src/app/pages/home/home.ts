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
  userName: string | null = null;
  userId: string | null = null;
  constructor(private auth: AuthService, private router: Router) {
  }

  ngOnInit() {
    this.userName = this.auth.currentUser?.displayName || 'Usuario sin nombre';
    this.userId = this.auth.currentUser?.uid || 'UID no disponible';
    console.log('Usuario actual:', this.userName, 'ID:', this.userId);
    console.log(this.auth.currentUser?.email);

  }
  

  async logout() {
    await this.auth.logout();
    this.router.navigate(['/login']);
  }
  
}
