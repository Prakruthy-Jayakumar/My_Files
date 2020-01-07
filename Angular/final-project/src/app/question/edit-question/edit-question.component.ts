import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router} from '@angular/router';

import { Question, QuestionDetails } from '../../questions';
import { UserService } from '../../user.service';

@Component({
  selector: 'app-edit-question',
  templateUrl: './edit-question.component.html',
  styleUrls: ['./edit-question.component.css']
})
export class EditQuestionComponent implements OnInit {

  constructor(
    private route: ActivatedRoute,
    private userserv: UserService,
    private router: Router
      
  ) { }

  ngOnInit() {
    if(!this.userserv.isLoggedIn()) {
      this.router.navigate(['/login']);
    } else{
      this.editquestion();
    }
  }

  result:Question;

  submitted = false;

  editForm() { 
    this.submitted = true; 
    this.userserv.updateQuestion(this.result).subscribe();
  }

  editquestion(){
    const id = +this.route.snapshot.paramMap.get('id');
    this.userserv.editQuestion(id).subscribe(result => this.result = result);
  }

}
 