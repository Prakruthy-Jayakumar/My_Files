import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import { Router } from '@angular/router';

import { UserService } from '../../user.service';
import { Answer, Question } from '../../questions';

@Component({
  selector: 'app-deletequestion',
  templateUrl: './deletequestion.component.html',
  styleUrls: ['./deletequestion.component.css']
})
export class DeletequestionComponent implements OnInit {

    constructor(
      private route:ActivatedRoute,
      private router:Router,
      private location: Location,
      private userSer: UserService
    ) { }
  

  ngOnInit() {
    this.deleteQuestion();
  }
  ques: Question;

  deleteQuestion(){
    console.log("haiiiiiii");
    const id = +this.route.snapshot.paramMap.get('id');
    console.log(id);
    this.userSer.deleteQuestion(this.ques,id).subscribe(()=>this.goBack());
}
goBack(): void{
  this.location.back();
}



}