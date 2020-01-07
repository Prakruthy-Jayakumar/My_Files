import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientModule }    from '@angular/common/http';
import { FormsModule }   from '@angular/forms';

import { LoginComponent } from './login/login.component';
import { HomeComponent } from './home/home.component';
import { RegisterComponent } from './register/register.component';
import { MessagesComponent } from './messages/messages.component';
import { AskQuestionComponent } from './question/ask-question/ask-question.component';
import { ListQuestionComponent } from './question/list-question/list-question.component';
import { ShowQuestionComponent } from './question/show-question/show-question.component';
import { EditQuestionComponent } from './question/edit-question/edit-question.component';
import { AnswerQuestionComponent } from './question/answer-question/answer-question.component';

import { MyQuestionsComponent } from './question/my-questions/my-questions.component';
import { UnlikeQuestionComponent } from './question/unlike-question/unlike-question.component';
import { LikeQuestionComponent } from './question/like-question/like-question.component';
import { QuestionSearchComponent } from './question/question-search/question-search.component';

import { EditAnswerComponent } from './anwsers/edit-answer/edit-answer.component';
import { AnswerByMeComponent } from './anwsers/answer-by-me/answer-by-me.component';
import { DeleteanswerComponent } from './anwsers/deleteanswer/deleteanswer.component';
import { DeletequestionComponent } from './question/deletequestion/deletequestion.component';




@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    HomeComponent,
    RegisterComponent,
    MessagesComponent,
    AskQuestionComponent,
    ListQuestionComponent,
    ShowQuestionComponent,
    EditQuestionComponent,
    AnswerQuestionComponent,
    MyQuestionsComponent,
    UnlikeQuestionComponent,
    LikeQuestionComponent,
    QuestionSearchComponent,
    
    EditAnswerComponent,
    AnswerByMeComponent,
    DeleteanswerComponent,
    DeletequestionComponent,
  
  ],
  imports: [
    BrowserModule,
    FormsModule,
    AppRoutingModule,
    HttpClientModule,
 
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
