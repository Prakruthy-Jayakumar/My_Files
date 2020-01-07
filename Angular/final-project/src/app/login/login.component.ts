import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Location } from '@angular/common';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { UserService } from '../user.service';
import { User } from '../user';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private location: Location,
    private userSer: UserService
  ) { }

  ngOnInit() {
  }


  login(user_details:User){
    console.log(user_details);
    this.userSer.loginAction(user_details).subscribe( response => 
      {
        console.log(response);
          var userid: any = response.user.id;
           localStorage.setItem('uid',userid);
           console.log(localStorage.getItem('uid', userid));
            localStorage.setItem('user_token',response.token);
            console.log(response);

                      
}
    )}
}