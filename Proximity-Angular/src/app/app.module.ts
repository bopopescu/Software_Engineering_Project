import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { routes } from './app-routing.module';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MaterialModule } from './material.module';
import { FlexLayoutModule } from '@angular/flex-layout';

import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { LoginPageComponent } from './login-page/login-page.component';
import { CreateAccountComponent } from './create-account/create-account.component';
import { ResetPasswordComponent } from './reset-password/reset-password.component';
import { MapPageComponent } from './map-page/map-page.component';
import { MessagingPageComponent } from './messaging-page/messaging-page.component';
import { FeedPageComponent } from './feed-page/feed-page.component';
import { ProfilePageComponent } from './profile-page/profile-page.component';
import { JwtInterceptor } from './models/jwt-interceptor';
import { LogoutDialogComponent } from './logout-dialog/logout-dialog.component';
import { HomePageComponent } from './home-page/home-page.component';
import { PostComponent } from './post/post.component';
import { EventPageComponent } from './event-page/event-page.component';
import { CreatePostDialogComponent } from './create-post-dialog/create-post-dialog.component';
import { EventsComponent } from './events/events.component';
import { UserService } from './services/user.service';


@NgModule({
  declarations: [
    AppComponent,
    LoginPageComponent,
    CreateAccountComponent,
    ResetPasswordComponent,
    MapPageComponent,
    MessagingPageComponent,
    FeedPageComponent,
    ProfilePageComponent,
    LogoutDialogComponent,
    HomePageComponent,
    PostComponent,
    CreatePostDialogComponent,
    EventPageComponent,
    EventsComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    RouterModule.forRoot(routes),
    HttpClientModule,
    BrowserAnimationsModule,
    MaterialModule,
    FlexLayoutModule
  ],
  providers: [{ provide: HTTP_INTERCEPTORS, useClass: JwtInterceptor, multi: true },
              UserService],
  bootstrap: [AppComponent],
  entryComponents: [LogoutDialogComponent]
})
export class AppModule { }
