import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DeleteanswerComponent } from './deleteanswer.component';

describe('DeleteanswerComponent', () => {
  let component: DeleteanswerComponent;
  let fixture: ComponentFixture<DeleteanswerComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DeleteanswerComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DeleteanswerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
