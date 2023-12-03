import { Injectable } from '@angular/core';
import {ValidationErrors} from "@angular/forms";

@Injectable({
  providedIn: 'root'
})
export class ErorrServiceService {

  constructor() { }

  getErrorMessage(fieldname: string, error: ValidationErrors | null | undefined): string {
    if (error && error['required']) {
      return `${fieldname} is required`;
    } else if (error && error['email']) {
      return `${fieldname} should be a valid email address`;
    } else if (error && error['pattern']) {
      return `${fieldname} should match : 10 number`;
    } else if (error && error['min']) {
      return `${fieldname} should be greater than or equal to ${error['min']['min']}`;
    } else if (error && error['max']) {
      return `${fieldname} should be less than or equal to ${error['max']['max']}`;
    } else {
      return '';
    }
  }
}
