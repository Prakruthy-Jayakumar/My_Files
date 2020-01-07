import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';


import { Question, Answer } from '../../questions';
import { UserService } from '../../user.service';

@Component({
  selector: 'app-show-question',
  templateUrl: './show-question.component.html',
  styleUrls: ['./show-question.component.css']
})
export class ShowQuestionComponent implements OnInit {

  constructor(
    private route: ActivatedRoute,
    private location: Location,
    private userserv: UserService
  ) { }

  ngOnInit() {
    this.showquestion();
  }

 result:Question;
 numberOfLikes: number=0;
 
  showquestion(){
   
    const id = +this.route.snapshot.paramMap.get('id');
    this.userserv.showQuestion(id).subscribe( response => this.result= response );
  }

  likequestion(){
    this.numberOfLikes++;
  }
  unlikequestion(){
    this.numberOfLikes--;
  }
  
  goBack(): void{
    this.location.back();
  }
}