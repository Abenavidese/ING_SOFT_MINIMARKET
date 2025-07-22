import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CajaInfo } from './caja-info';

describe('CajaInfo', () => {
  let component: CajaInfo;
  let fixture: ComponentFixture<CajaInfo>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CajaInfo]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CajaInfo);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
