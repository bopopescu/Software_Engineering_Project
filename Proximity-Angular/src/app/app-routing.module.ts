//written by: John Oatey
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
import { HomePageComponent} from './home-page/home-page.component';
import { AuthGuard } from './services/auth.guard';
import { EventPageComponent } from './event-page/event-page.component';

export const routes: Routes = [
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: 'login', component: LoginPageComponent },
  { path: 'create-account', component: CreateAccountComponent},
  { path: 'reset-password', component: ResetPasswordComponent},
  { path: 'map', component: MapPageComponent, canActivate: [AuthGuard]},
  { path: 'messaging', component: MessagingPageComponent, canActivate: [AuthGuard] },
  { path: 'feed', component: FeedPageComponent, canActivate: [AuthGuard]  },
  { path: 'home', component: HomePageComponent},
  { path: 'events', component: EventPageComponent, canActivate: [AuthGuard]},
  { path: 'profile/:userId', component: ProfilePageComponent, canActivate: [AuthGuard]  }

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
