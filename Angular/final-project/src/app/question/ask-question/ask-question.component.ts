import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import { Router } from '@angular/router';

import { UserService } from '../../user.service';
import { Question } from '../../questions';


@Component({
  selector: 'app-ask-question',
  templateUrl: './ask-question.component.html',
  styleUrls: ['./ask-question.component.css']
})
export class AskQuestionComponent implements OnInit {

  constructor(
    private route:ActivatedRoute,
    private router:Router,
    private location: Location,
    private userSer: UserService
  ) { }

  ngOnInit() {
    if(!this.userSer.isLoggedIn()) {
      this.router.navigate(['/login']);
    } 
  }

  question(ques_details:Question){
    console.log(ques_details);
    this.userSer.questionAction(ques_details).subscribe( response => {
    console.log(response);
    
  }
  );

}
}