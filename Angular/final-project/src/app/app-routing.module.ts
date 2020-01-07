import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { HomeComponent } from './home/home.component';
import { RegisterComponent } from './register/register.component';
import { ListQuestionComponent } from './question/list-question/list-question.component';
import { AnswerQuestionComponent } from './question/answer-question/answer-question.component';
import { AskQuestionComponent } from './question/ask-question/ask-question.component';
import { ShowQuestionComponent } from './question/show-question/show-question.component';
import { MyQuestionsComponent } from './question/my-questions/my-questions.component';
import { EditQuestionComponent } from './question/edit-question/edit-question.component';
import { EditAnswerComponent } from './anwsers/edit-answer/edit-answer.component';
import { AnswerByMeComponent } from './anwsers/answer-by-me/answer-by-me.component';
import { UnlikeQuestionComponent } from './question/unlike-question/unlike-question.component';
import { LikeQuestionComponent } from './question/like-question/like-question.component';
import { DeleteanswerComponent } from './anwsers/deleteanswer/deleteanswer.component';
import { DeletequestionComponent } from './question/deletequestion/deletequestion.component';
import { QuestionSearchComponent } from './question/question-search/question-search.component';

const routes: Routes = [
 
  { path: '', component: HomeComponent  },

  { path: 'register', component: RegisterComponent  },
  { path: 'login', component: LoginComponent },
  
  { path: 'listquestions', component: ListQuestionComponent },
  { path: 'askquestions', component: AskQuestionComponent },

  { path: 'showquestions/:id', component: ShowQuestionComponent },
  { path: 'editquestions/:id', component: EditQuestionComponent },
  {path: 'deletequestions/:id', component: DeletequestionComponent},
  { path: 'addanswers/:id', component: AnswerQuestionComponent },
  {path: 'myquestions', component: MyQuestionsComponent},
  {path: 'answeredbyme', component: AnswerByMeComponent},

  {path: 'searchquestion', component:QuestionSearchComponent},

  { path: 'editanswers/:id', component: EditAnswerComponent },
  {path: 'deleteanswer/:id', component: DeleteanswerComponent},
  //{path: '/', component: AnswerByMeComponent}
  
  //{path: 'unlikequestions/:id', component: UnlikeQuestionComponent},
  //{path: 'likequestions/:id', component: LikeQuestionComponent},

 
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
