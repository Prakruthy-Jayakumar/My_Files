import { Component } from '@angular/core';
import { UserService } from './user.service';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  constructor(private userService:UserService){

  }
  title = 'final-project';
  
  get isLoggedIn() { return this.userService.isLoggedIn(); }

  logout(){
    this.userService.logoutUser();
  }
}
