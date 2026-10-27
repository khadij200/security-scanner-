import { Component, signal } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { ScannerService } from './services/scanner';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [FormsModule, CommonModule],
  templateUrl: './app.html',
  styleUrl: './app.scss'
})
export class App {
  url = '';
  result = signal<any>(null);
  loading = signal(false);
  explanation = signal<string | null>(null);
  explaining = signal(false);

  constructor(private scanner: ScannerService) {}

  runScan() {
    if (!this.url) return;
    this.loading.set(true);
    this.result.set(null);
    this.explanation.set(null);
    this.scanner.scanUrl(this.url).subscribe({
      next: (res) => {
        this.result.set(res);
        this.loading.set(false);
      },
      error: (err) => {
        this.result.set({ error: 'صار خطأ بالاتصال، تأكد إن الباك اند شغال' });
        this.loading.set(false);
      }
    });
  }

  explainScan() {
    const res = this.result();
    if (!res) return;

    this.explaining.set(true);
    this.explanation.set(null);

    const headersText = this.getHeadersList()
      .map(h => `${h.key}: ${h.value ? 'موجود' : 'غير موجود'}`)
      .join(', ');

    const sslText = res.ssl?.valid ? 'صحيحة' : 'غير صحيحة';

    this.scanner.explainResult(res.url, headersText, sslText).subscribe({
      next: (r: any) => {
        this.explanation.set(r.explanation || r.error);
        this.explaining.set(false);
      },
      error: () => {
        this.explanation.set('صار خطأ أثناء توليد الشرح');
        this.explaining.set(false);
      }
    });
  }

  getHeadersList() {
    const res = this.result();
    if (!res || !res.security_headers) return [];
    return Object.keys(res.security_headers).map(key => ({
      key,
      value: res.security_headers[key]
    }));
  }
}