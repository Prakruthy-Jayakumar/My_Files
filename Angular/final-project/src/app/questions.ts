export class QuestionDetails {
    
    current_page:number;
    data:Array<Question>;
    first_page_url:String;  
    questions?:string;  
}

export class Questions {
    current_page:number;
    data:Array<Question>;
    first_page_url:String;  
   
}

export class Question {
    id:number;
    user_id:number;
    title: string;
    question: string;
    answers:Array<Answer>;
}

export class Answer {
    id: number;
    user_id: number;
    question_id: number;
    answer: string;
}