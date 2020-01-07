import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AnswerByMeComponent } from './answer-by-me.component';

describe('AnswerByMeComponent', () => {
  let component: AnswerByMeComponent;
  let fixture: ComponentFixture<AnswerByMeComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AnswerByMeComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AnswerByMeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
