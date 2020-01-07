import { Injectable } from '@angular/core';

import { Observable, of, from } from 'rxjs';
import { catchError, map, tap } from 'rxjs/operators';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { MessageService } from './message.service';

import { User } from './user';
import {Answer, Question , Questions, QuestionDetails} from './questions';


const httpOptions = {
  headers: new HttpHeaders(
    { 'Content-Type': 'application/json',
     'Authorization': 'Bearer '+localStorage.getItem("user_token") 
     
    })
};


@Injectable({
  providedIn: 'root'
})
export class UserService {
  constructor(
    private http: HttpClient,
    private messageService: MessageService
  ) { }


  private registerUrl = "http://forum.mashuptest.com/api/register"
  private loginUrl = "http://forum.mashuptest.com/api/login"
  private askquestionUrl ="http://forum.mashuptest.com/api/question"
  private listUrl = "http://forum.mashuptest.com/api/question"
  private editUrl ="http://forum.mashuptest.com/api/question"
  private showUrl="http://forum.mashuptest.com/api/question"
  private answerUrl = "http://forum.mashuptest.com/api/question"
  private myquestionUrl ="http://forum.mashuptest.com/api/question/my-questions"
  private deletequestionUrl="http://forum.mashuptest.com/api/question"
  private editanswerUrl ="http://forum.mashuptest.com/api/answer"
  private myanswerUrl ="http://forum.mashuptest.com/api/question/answered-by-me"
  private deleteanswerurl= "http://forum.mashuptest.com/api/answer"
  private likequestionUrl ="http://forum.mashuptest.com/api/question"
  private questionsearchUrl = "http://forum.mashuptest.com/api/question/search?keyword="


//Signing Up
  registerAction(user_details:User): Observable<User> {
    this.messageService.add('Registration Successful');
    return this.http.post<User>(this.registerUrl,user_details)
  }
//Log In
  loginAction(user_details:User): Observable<User> {
    this.messageService.add('Login Successful');
    return this.http.post<User>(this.loginUrl,user_details)
  }
//Ask Questions
  questionAction(ques_details:Question): Observable<User> {
    this.messageService.add('Added question Successful');
    return this.http.post<User>(this.askquestionUrl,ques_details,httpOptions)
  }
//List Questions
  listQuestion(): Observable<QuestionDetails[]> {
    return this.http.get<QuestionDetails[]>(this.listUrl)
  }
//My questions
  myQuestion(): Observable<any> {
  return this.http.get<any>(this.myquestionUrl,httpOptions)
  }

//My answers
myAnswer(): Observable<Questions[]> {
  return this.http.get<Questions[]>(this. myanswerUrl,httpOptions)
  }
  
//Show individual question details
  showQuestion(id:number): Observable<Question> {
    const url =`${this.showUrl}/${id}`;
    return this.http.get<Question>(url)
  }

//Edit the question details
  updateQuestion (x: Question): Observable<any> {
    const url =`${this.editUrl}/${x.id}`;
    return this.http.put(url, x, httpOptions)
  }

  editQuestion(id:number): Observable<Question> {
    const url =`${this.editUrl}/${id}`;
    return this.http.get<Question>(url)
}

//Edit answers

editAnswer(result,id): Observable<any> {
  const url =`${this.editanswerUrl}/${id}`;
  return this.http.put(url,result,httpOptions).pipe(
    tap(_ => this.log(`updated answer id=${(id)}`)),
    catchError(this.handleError<any>('Edit Answer'))

  );
}
  private handleError<T> (operation = 'operation', result?: T) {
     return (error: any): Observable<T> => {
    
       // TODO: send the error to remote logging infrastructure
       // console.error(error); // log to console instead
    
       // TODO: better job of transforming error for user consumption
       this.log(`${operation} failed: ${error.message}`);
    
       // Let the app keep running by returning an empty result.
       return of(result as T);
     };
   }
     log(message:string){
       this.messageService.add(message);


}
//Add answers
answerAction(ans_details:Answer,id:number): Observable<User> {
 
  this.messageService.add('Added answer Successfully');
  const url =`${this.answerUrl}/${id}/answer`;
  return this.http.post<User>(url,ans_details,httpOptions)
}

//Delete answer
deleteAnswer (ans,id): Observable<any> {
  const url = `${this.deleteanswerurl}/${id}`;

  return this.http.delete(url, httpOptions).pipe(
    tap(_ => this.log(`deleted answer id=${id}`)),
    catchError(this.handleError('deletAnswer'))
  );
}

//Delete Question
deleteQuestion (ques,id): Observable<any> {
  const url = `${this.deletequestionUrl}/${id}`;

  return this.http.delete(url, httpOptions).pipe(
    tap(_ => this.log(`deleted question id=${id}`)),
    catchError(this.handleError('Delete Question'))
  );
}


//like question
likeQuestion(ques,id): Observable<any>{
  const url = `${this.likequestionUrl}/${id}/like`;

  return this.http.post(url,httpOptions).pipe(
    tap(_ => this.log(`liked question id=${id}`)),
    catchError(this.handleError('Like Question'))
  );
}
//unlike question
unlikeQuestion(ques,id): Observable<any>{
  const url = `${this.likequestionUrl}/${id}/like`;

  return this.http.post(url,httpOptions).pipe(
    tap(_ => this.log(`unliked question id=${id}`)),
    catchError(this.handleError('unLike Question'))
  );
}

//Question-serach
  searchQuestion(key): Observable<any>{
    const url=`${this.questionsearchUrl}${key.search}`;
    console.log(url);
    return this.http.get<any>(url, key);
  }


//For logged in users
isLoggedIn(){
  return localStorage.getItem('user_token');
  
}
//Logout User
logoutUser(){
  return localStorage.removeItem('user_token');
}

getuserid(){
  return localStorage.getItem('uid');
}



}
