import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { LikeQuestionComponent } from './like-question.component';

describe('LikeQuestionComponent', () => {
  let component: LikeQuestionComponent;
  let fixture: ComponentFixture<LikeQuestionComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ LikeQuestionComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LikeQuestionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
