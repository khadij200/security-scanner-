from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import ssl
import socket
from groq import Groq
from dotenv import load_dotenv
import os
import re
from datetime import datetime
load_dotenv()
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/hello")
def hello():
    return {"message": "الباك اند يشتغل تمام"}

@app.get("/api/scan")
def scan(url: str):
    try:
        response = requests.get(url, timeout=5)
        headers = response.headers

        checks = {
            "Content-Security-Policy": "Content-Security-Policy" in headers,
            "X-Frame-Options": "X-Frame-Options" in headers,
            "Strict-Transport-Security": "Strict-Transport-Security" in headers,
            "X-Content-Type-Options": "X-Content-Type-Options" in headers,
        }

        ssl_info = check_ssl(url)

        return {
            "url": url,
            "status_code": response.status_code,
            "security_headers": checks,
            "ssl": ssl_info
        }
    except Exception as e:
        return {"error": str(e)}


def check_ssl(url: str):
    try:
        hostname = url.replace("https://", "").replace("http://", "").split("/")[0]
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                expire_date = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
                days_left = (expire_date - datetime.now()).days

                return {
                    "valid": True,
                    "expires": expire_date.strftime('%Y-%m-%d'),
                    "days_left": days_left
                }
    except Exception as e:
        return {
            "valid": False,
            "error": str(e)
        }
def clean_text(text: str) -> str:
    # يشيل فقط الأحرف من لغات مو عربي/إنجليزي (صيني، ياباني، روسي، إلخ)
    cleaned = re.sub(r'[\u4e00-\u9fff\u3040-\u30ff\u0400-\u04FF]', '', text)
    return cleaned

@app.get("/api/explain")
def explain(url: str, headers: str, ssl_valid: str):
    try:
        prompt = f"""
أنت خبير أمن سيبراني. اكتب تقرير مختصر بالعربية الفصحى فقط عن حالة أمان موقع.

بيانات الفحص:
- الموقع: {url}
- Security Headers: {headers}
- شهادة SSL: {ssl_valid}

قواعد صارمة:
- اكتب بالعربية فقط، ممنوع أي لغة أخرى غير العربية والإنجليزية
- المصطلحات التقنية الإنجليزية تكتب لحالها بين قوسين، مثال: (X-Frame-Options)
- لا تدمج كلمة إنجليزية وسط جملة عربية بدون قوسين
- لا تستخدم رمز \\n، استخدم فقرات حقيقية منفصلة

اكتب التقرير بهذا الشكل بالضبط:

الحالة العامة:
[فقرة واحدة قصيرة، جملتين كحد أقصى، تصف وضع الموقع الأمني بشكل عام]

التوصيات:
- [توصية أولى قصيرة]
- [توصية ثانية قصيرة]
- [توصية ثالثة قصيرة إن وجدت]
"""
        response = groq_client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[{"role": "user", "content": prompt}],
        )

        explanation = response.choices[0].message.content
        explanation = clean_text(explanation)
        return {"explanation": explanation}

    except Exception as e:
        return {"error": str(e)}