import { NgModule } from '@angular/core';

import {
  MatButtonModule,
  MatMenuModule,
  MatToolbarModule,
  MatIconModule,
  MatCardModule,
  MatListModule,
  MatSidenavModule,
  MatFormFieldModule,
  MatInputModule

} from '@angular/material';




@NgModule({
  imports: [
    MatIconModule,
    MatListModule,
    MatToolbarModule,
    MatSidenavModule
  ],
  exports: [
    MatButtonModule,
    MatMenuModule,
    MatToolbarModule,
    MatIconModule,
    MatCardModule,
    MatListModule,
    MatSidenavModule,
    MatFormFieldModule,
    MatInputModule
  ]
})
export class MaterialModule {}