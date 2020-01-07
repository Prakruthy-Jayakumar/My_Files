import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import { Router } from '@angular/router';

import { UserService } from '../../user.service';
import { Answer } from '../../questions';


@Component({
  selector: 'app-deleteanswer',
  templateUrl: './deleteanswer.component.html',
  styleUrls: ['./deleteanswer.component.css']
})
export class DeleteanswerComponent implements OnInit {

    constructor(
      private route:ActivatedRoute,
      private router:Router,
      private location: Location,
      private userSer: UserService
    ) { }
  

  ngOnInit() {
    this.deleteAnswer();
  }
  ans: Answer;

  deleteAnswer(){
    console.log("haiiiiiii");
    const id = +this.route.snapshot.paramMap.get('id');
    console.log(id);
    this.userSer.deleteAnswer(this.ans,id).subscribe(()=>this.goBack());
}
goBack(): void{
  this.location.back();
}



}
