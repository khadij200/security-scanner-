import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ScannerService {
  private apiUrl = 'http://localhost:8000/api/scan';
  private explainUrl = 'http://localhost:8000/api/explain';

  constructor(private http: HttpClient) {}

  scanUrl(url: string) {
    return this.http.get(`${this.apiUrl}?url=${url}`);
  }

  explainResult(url: string, headers: string, sslValid: string) {
    return this.http.get(
      `${this.explainUrl}?url=${url}&headers=${headers}&ssl_valid=${sslValid}`
    );
  }
}