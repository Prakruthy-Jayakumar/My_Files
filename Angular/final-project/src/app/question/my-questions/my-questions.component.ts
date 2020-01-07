import { Component, OnInit } from '@angular/core';
import { UserService } from '../../user.service';
import { ActivatedRoute } from '@angular/router';
import { Question, Questions } from '../../questions';
import { Location } from '@angular/common';
import { Router } from '@angular/router';

@Component({
  selector: 'app-my-questions',
  templateUrl: './my-questions.component.html',
  styleUrls: ['./my-questions.component.css']
})
export class MyQuestionsComponent implements OnInit {

    constructor(
      private route:ActivatedRoute,
      private router:Router,
      private location: Location,
      private userSer: UserService
    ) { }

    ngOnInit() {
      if(!this.userSer.isLoggedIn()) {
        this.router.navigate(['/login']);
      } else{
        this.myquestion();

    }}

    result:Questions[];
    
   

  myquestion(){
    console.log("testtt")
    this.userSer.myQuestion().subscribe(x => this.result = x.questions);
  }  

  
}