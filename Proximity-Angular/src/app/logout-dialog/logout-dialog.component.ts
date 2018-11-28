import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import {MatDialog, MatDialogRef, MAT_DIALOG_DATA} from '@angular/material';

@Component({
  selector: 'app-logout-dialog',
  templateUrl: './logout-dialog.component.html',
  styleUrls: ['./logout-dialog.component.css']
})
export class LogoutDialogComponent implements OnInit {

  constructor(private router: Router, public dialogRef: MatDialogRef<LogoutDialogComponent>) { }

  ngOnInit() {
  }

  onYesClick(){
    this.router.navigateByUrl("/login");
    this.dialogRef.close();
  }

  onNoClick(){
    this.dialogRef.close();
  }

}
