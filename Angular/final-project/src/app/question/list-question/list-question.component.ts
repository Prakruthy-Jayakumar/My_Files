import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';

import { UserService } from '../../user.service';
import { QuestionDetails } from '../../questions';

@Component({
  selector: 'app-list-question',
  templateUrl: './list-question.component.html',
  styleUrls: ['./list-question.component.css']
})
export class ListQuestionComponent implements OnInit {

  constructor(
    private route: ActivatedRoute,
    private location: Location,
    private userSer: UserService
  ) { }

  ngOnInit() {
    this.listquestion();
  }
  
  myArray:QuestionDetails[];

  listquestion(){
    this.userSer.listQuestion().subscribe(x => this.myArray = x);
  }
}

