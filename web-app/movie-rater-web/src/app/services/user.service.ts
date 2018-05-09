import { environment } from './../../environments/environment.prod';
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserService {

HttpHeaders = new HttpHeaders({'Content-Type': 'application/json; charset=utf-8'});
baseUrl: string = environment.apiUrl;

  constructor(private http: HttpClient) { }

  loginUser(userData: any): Observable<any> {
    return this.http.post(this.baseUrl + 'authenticate/', userData, {headers: this.HttpHeaders});
  }
}
