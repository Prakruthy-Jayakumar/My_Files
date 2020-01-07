import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Location } from '@angular/common';

import { UserService } from '../../user.service';
import { Answer } from '../../questions';

@Component({
  selector: 'app-answer-question',
  templateUrl: './answer-question.component.html',
  styleUrls: ['./answer-question.component.css']
})
export class AnswerQuestionComponent implements OnInit {

  constructor(
    private route: ActivatedRoute,
    private location: Location,
    private userSer: UserService,
    private router:Router,
  ) { }

  ngOnInit() {
    if(!this.userSer.isLoggedIn()) {
      this.router.navigate(['/login']);
    } 
  }

  answer(ans_details:Answer){
  
   const id = +this.route.snapshot.paramMap.get('id');
  this.userSer.answerAction(ans_details,id).subscribe( response => {
  console.log(response);
  }
  );

  }
}