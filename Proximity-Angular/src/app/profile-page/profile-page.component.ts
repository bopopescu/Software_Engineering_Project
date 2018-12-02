import { Component, OnInit } from '@angular/core';
import { DataService } from '../services/data.service';
import { ActivatedRoute } from '@angular/router';
import { FormBuilder } from '@angular/forms';
import { Observable } from "rxjs";
import { User } from '../models/user';
import { UserService } from '../services/user.service';

@Component({
  selector: 'app-profile-page',
  templateUrl: './profile-page.component.html',
  styleUrls: ['./profile-page.component.css', '../app.component.css']
})
export class ProfilePageComponent implements OnInit {

  constructor(private dataService: DataService, private activatedRoute: ActivatedRoute
    , private fb: FormBuilder, private userService: UserService) { }

    profileData = this.fb.group({
      firstName: [''],
      lastName: [''],
      email: [''],
    })

    // profile: Observable<Friend>;
    profile: User



  ngOnInit() {
    var id: Number = Number.parseInt(this.activatedRoute.snapshot.url[1].path);
    this.profileData.disable();
    // this.dataService.getProfileInfo(id)
    //   .subscribe(info => {
    //     this.profile = info;
    //   })

    setTimeout(() => {
      if(id == 5){
        this.profile =  {
          firstName: "Miley",
          lastName: "Cyrus",
          id: 5,
          email: "WreckingHoes@Career.gov",
          distance: 50,
          posts: [
            {
              body: "Something I just wonder what would have happened if I focused more on my career.",
              name: "Miley Cyrus",
              title: "My career is a dump now...",
            },
            {
              body: "Something something daddy issues. JKFDS:JFK:LDFJSK L: Jfkljfakldsfj iaj eilj afis;j flsakjiewjo pdjfkad;slfj a;sdjfs da;fjkas; fjdakl ;fj",
              name: "Miley Cyrus",
              title: "My dad sucks"
            }
          ],
          fullName: "Miley Cyrus"          
        }
        console.log(this.profile);
      }
    }, 3000);
  }

}
