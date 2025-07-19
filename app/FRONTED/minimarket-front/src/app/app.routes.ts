import { Routes } from '@angular/router';
import { LoginComponent } from './pages/login/login';
import { HomeComponent } from './pages/home/home';
import { Products } from './pages/products/products';
import { authGuard } from './guards/auth-guard';
import { Providers } from './pages/providers/providers';
import { Categories } from './pages/categories/categories'; 

export const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: 'home', component: HomeComponent, canActivate: [authGuard] },
  { path: 'products', component: Products, canActivate: [authGuard] },
  { path: 'providers' , component: Providers, canActivate: [authGuard] },
  { path: 'categories', component: Categories, canActivate: [authGuard] },
  { path: '**', redirectTo: 'login' }
]; 
