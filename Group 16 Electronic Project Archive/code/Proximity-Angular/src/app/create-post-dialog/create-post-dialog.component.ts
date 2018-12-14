//written by: John Oatey
import { Component, OnInit, Inject } from '@angular/core';
import {MAT_DIALOG_DATA, MatDialogRef} from '@angular/material';
import { FormBuilder } from '@angular/forms';

@Component({
  selector: 'app-create-post-dialog',
  templateUrl: './create-post-dialog.component.html',
  styleUrls: ['./create-post-dialog.component.css']
})
export class CreatePostDialogComponent implements OnInit {

  constructor(@Inject(MAT_DIALOG_DATA) public data: any, public dialogRef: MatDialogRef<CreatePostDialogComponent>, private fb: FormBuilder) { }

  createPost = this.fb.group({
    body: [''],
    title: ['']
  })
  
  ngOnInit() {
  }

  cancel(){
    this.dialogRef.close();
  }

  create(){
    console.log("Trying");
    this.dialogRef.close(this.createPost);
  }
}
