import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import { Router } from '@angular/router';

import { UserService } from '../../user.service';
import { Question } from '../../questions';

@Component({
  selector: 'app-unlike-question',
  templateUrl: './unlike-question.component.html',
  styleUrls: ['./unlike-question.component.css']
})
export class UnlikeQuestionComponent implements OnInit {

    constructor(
      private route:ActivatedRoute,
      private router:Router,
      private location: Location,
      private userSer: UserService
    ) { }
  
  
  ngOnInit() {
    this.unlikequestion();
  }
  ques: Question;
  
  unlikequestion(){
    console.log("haiiiiiii");
    const id = +this.route.snapshot.paramMap.get('id');
    console.log(id);
    this.userSer.unlikeQuestion(this.ques,id).subscribe(()=>this.goBack());
  }
  goBack(): void{
  this.location.back();
  }
  
  
  
  }
