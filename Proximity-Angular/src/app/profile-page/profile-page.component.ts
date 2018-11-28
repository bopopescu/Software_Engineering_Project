import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';
import { ActivatedRouteSnapshot } from '@angular/router';
import { FormBuilder } from '@angular/forms';
import { Observable } from "rxjs";
import { Friend } from '../models/friend';

@Component({
  selector: 'app-profile-page',
  templateUrl: './profile-page.component.html',
  styleUrls: ['./profile-page.component.css', '../app.component.css']
})
export class ProfilePageComponent implements OnInit {

  constructor(private dataService: DataService, private activatedRoute: ActivatedRouteSnapshot
    , private fb: FormBuilder) { }

    profileData = this.fb.group({
      firstName: [''],
      lastName: [''],
      email: [''],

    })

    profile: Observable<Friend>;



  ngOnInit() {
    var id: Number = this.activatedRoute.params.id;
    // this.dataService.getProfileInfo(id)
    //   .subscribe(info => {
    //     this.profile = info;
    //   })
  }

}
