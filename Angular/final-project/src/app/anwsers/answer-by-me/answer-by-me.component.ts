import { Component, OnInit } from '@angular/core';
import { UserService } from '../../user.service';
import { ActivatedRoute } from '@angular/router';
import { Answer, Questions } from '../../questions';
import { Location } from '@angular/common';
import { Router } from '@angular/router';
@Component({
  selector: 'app-answer-by-me',
  templateUrl: './answer-by-me.component.html',
  styleUrls: ['./answer-by-me.component.css']
})
export class AnswerByMeComponent implements OnInit {

  constructor(
    private route:ActivatedRoute,
    private router:Router,
    private location: Location,
    private userSer: UserService
  ) { }

  ngOnInit() {
    if(!this.userSer.isLoggedIn()) {
      this.router.navigate(['/login']);
    } else{
      this.myanswer();
    }
  }

  result:Questions[];
 

myanswer(){
  this.userSer.myAnswer().subscribe(x => {
    console.log(x);
  }
  )
}  
}