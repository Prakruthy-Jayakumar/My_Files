import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import { Router } from '@angular/router';

import { UserService } from '../../user.service';
import { Question } from '../../questions';
@Component({
  selector: 'app-like-question',
  templateUrl: './like-question.component.html',
  styleUrls: ['./like-question.component.css']
})
export class LikeQuestionComponent implements OnInit {

  constructor(
    private route:ActivatedRoute,
    private router:Router,
    private location: Location,
    private userSer: UserService,
    
  ) { }


ngOnInit() {
  this.likequestion();
}
ques: Question;
numberOfLikes: number=0;

likequestion(){
  this.numberOfLikes++;
}
unlikequestion(){
  this.numberOfLikes--;
}
}
  // console.log("haiiiiiii");
  // const id = +this.route.snapshot.paramMap.get('id');
  // console.log(id);
  // this.userSer.likeQuestion(this.ques,id).subscribe(()=>this.goBack());
// }
// goBack(): void{
// this.location.back();
// }