import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';


import { UserService } from '../user.service';
import { User } from '../user';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})

export class RegisterComponent implements OnInit {

  constructor(
    private route: ActivatedRoute,
    private location: Location,
    private userSer: UserService
  ) { }

  ngOnInit() {
 
  }

  register(user_details:User){
    console.log("abcd");
    console.log(user_details);
    this.userSer.registerAction(user_details).subscribe( response => {
        console.log(response);
      }
    );

}
}
