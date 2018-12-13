//written by: John Oatey
import { Component, OnInit, Inject } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material';

@Component({
  selector: 'app-create-comment-dialog',
  templateUrl: './create-comment-dialog.component.html',
  styleUrls: ['./create-comment-dialog.component.css']
})
export class CreateCommentDialogComponent implements OnInit {

  constructor(@Inject(MAT_DIALOG_DATA) public data: any, public dialogRef: MatDialogRef<CreateCommentDialogComponent>, private fb: FormBuilder) { }

  ngOnInit() {
  }

  createComment = this.fb.group({
    body: ['']
  })

  cancel(){
    this.dialogRef.close();
  }

  create(){
    this.dialogRef.close(this.createComment.get('body').value);
  }

}
