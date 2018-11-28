import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Routes, Router } from '@angular/router';

import { LoginPageComponent } from './login-page/login-page.component';
import { CreateAccountComponent } from './create-account/create-account.component';
import { ResetPasswordComponent } from './reset-password/reset-password.component';
import { MapPageComponent } from './map-page/map-page.component';
import { MessagingPageComponent } from './messaging-page/messaging-page.component';
import { FeedPageComponent } from './feed-page/feed-page.component';
import { ProfilePageComponent } from './profile-page/profile-page.component';
import { AuthGuard } from './auth.guard';

export const routes: Routes = [
  { path: '', redirectTo: '/feed', pathMatch: 'full' },
  { path: 'login', component: LoginPageComponent },
  { path: 'create-account', component: CreateAccountComponent},
  { path: 'reset-password', component: ResetPasswordComponent},
  { path: 'map', component: MapPageComponent },
  { path: 'messaging', component: MessagingPageComponent, canActivate: [AuthGuard] },
  { path: 'feed', component: FeedPageComponent },
  { path: 'profile/:userId', component: ProfilePageComponent, canActivate: [AuthGuard]}
];

@NgModule({
  imports: [
    CommonModule,
    RouterModule,
    RouterModule.forRoot(routes)
  ],
  exports: [ RouterModule ],
})

export class AppRoutingModule { }
