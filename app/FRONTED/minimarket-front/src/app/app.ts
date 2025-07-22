import { Component, signal } from '@angular/core';
import { Router, RouterOutlet } from '@angular/router';
import { CommonModule } from '@angular/common';
import { Menu } from './pages/menu/menu';

@Component({
  selector: 'app-root',
  imports: [CommonModule, RouterOutlet, Menu],
  templateUrl: './app.html',
  styleUrl: './app.scss'
})
export class App {
  protected readonly title = signal('minimarket-front');

  constructor(private router: Router) {}

  get isAuthenticated(): boolean {
    return this.router.url !== '/login';
  }
}
