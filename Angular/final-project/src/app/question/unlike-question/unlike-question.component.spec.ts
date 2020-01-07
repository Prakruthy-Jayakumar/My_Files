import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { UnlikeQuestionComponent } from './unlike-question.component';

describe('UnlikeQuestionComponent', () => {
  let component: UnlikeQuestionComponent;
  let fixture: ComponentFixture<UnlikeQuestionComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ UnlikeQuestionComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(UnlikeQuestionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
