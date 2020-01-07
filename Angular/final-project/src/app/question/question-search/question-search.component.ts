import { Component, OnInit } from '@angular/core';
import { UserService } from '../../user.service';
import { ActivatedRoute } from '@angular/router';
import { Question, QuestionDetails} from '../../questions';
import { Location } from '@angular/common';
import { Router } from '@angular/router';

@Component({
  selector: 'app-question-search',
  templateUrl: './question-search.component.html',
  styleUrls: ['./question-search.component.css']
})
export class QuestionSearchComponent implements OnInit {
  constructor(
    private route:ActivatedRoute,
    private router:Router,
    private location: Location,
    private userSer: UserService
  ) { }

  ngOnInit() {


  }

 ques: QuestionDetails[];
  
 

searchquestion(key:string){
  console.log("testtt")
  console.log(key);
  this.userSer.searchQuestion(key).subscribe(x => 
    {
      this.ques = x.x,
    console.log(x.result.data);
}  
  );
}
}