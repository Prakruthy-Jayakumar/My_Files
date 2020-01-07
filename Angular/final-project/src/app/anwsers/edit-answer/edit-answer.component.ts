import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router} from '@angular/router';

import {Answer, Question, QuestionDetails } from '../../questions';
import { UserService } from '../../user.service';

@Component({
  selector: 'app-edit-answer',
  templateUrl: './edit-answer.component.html',
  styleUrls: ['./edit-answer.component.css']
})
export class EditAnswerComponent implements OnInit {

  constructor(
    private route: ActivatedRoute,
    private userserv: UserService,
    private router: Router
      
  ) { }

  ngOnInit() {
    if(!this.userserv.isLoggedIn()) {
   this.router.navigate(['/login']);
    } else{
   this.editanswer(this.result);
    }
  }

  result:Question[];

  editanswer(result){
    console.log("haiiiiiii");
    const id = +this.route.snapshot.paramMap.get('id');
    console.log(id);
    this.userserv.editAnswer(result,id).subscribe(response=> this.result = response);
  }

}