# 🔐 Security Scanner

A full-stack web application that performs basic website security checks and provides AI-powered security explanations and recommendations in Arabic.

The project is developed using **Angular** for the frontend, **Python FastAPI** for the backend, and **Groq AI** for generating security reports.

## Features

- **Website Security Scanning:** Analyze a website by entering its URL.
- **HTTP Status Code:** Display the HTTP response status of the scanned website.
- **Security Headers Analysis:** Check whether the following security headers are present:
  - Content-Security-Policy
  - X-Frame-Options
  - Strict-Transport-Security
  - X-Content-Type-Options
- **SSL Certificate Verification:** Check certificate validity, expiration date, and remaining days.
- **AI-Powered Security Reports:** Generate Arabic explanations and recommendations using the Groq API.
- **Arabic User Interface:** Present security scan results in a clear, user-friendly interface.

## Technologies Used

| Component | Technologies |
|---|---|
| Frontend | Angular, TypeScript, HTML, SCSS |
| Backend | Python, FastAPI |
| HTTP Requests | Requests |
| SSL Verification | Python SSL, Socket |
| AI Integration | Groq API |
| Environment Variables | python-dotenv |
| Development Tools | VS Code, Git, GitHub |

## Project Structure

```text
security-scanner/
├── backend/
│   ├── main.py
│   └── .env                 # Local only, not uploaded
├── frontscanner/
│   ├── public/
│   ├── src/
│   │   └── app/
│   │       └── services/
│   ├── angular.json
│   └── package.json
├── .gitignore
└── README.md
```

## Prerequisites

Before running the application, make sure you have installed:

- Python 3
- Node.js and npm
- Git
- A Groq API key for AI-powered reports

## Installation and Setup

### Step 1: Clone the Repository

Once the project is published on GitHub, clone its repository using the URL provided on the repository page.

Navigate to the project directory:

```bash
cd security-scanner
```

### Step 2: Set Up the Backend

Open a terminal and navigate to the backend directory:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**

```cmd
venv\Scripts\activate.bat
```

Install the required Python packages:

```bash
python -m pip install fastapi uvicorn requests groq python-dotenv
```

### Step 3: Configure the Groq API Key

Create a `.env` file inside the `backend` directory.

Add:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Replace the placeholder with your own Groq API key.

**Security:** Never commit `.env` files or API keys to GitHub.

### Step 4: Run the Backend

From the `backend` directory, run:

```bash
python -m uvicorn main:app --reload
```

The backend will start at:

http://127.0.0.1:8000

Test the backend:

http://127.0.0.1:8000/api/hello

Interactive API documentation:

http://127.0.0.1:8000/docs

Keep the backend terminal running.

### Step 5: Set Up the Frontend

Open a new terminal from the `security-scanner` directory.

Navigate to the Angular project:

```bash
cd frontscanner
```

Install dependencies:

```bash
npm install
```

Start the Angular development server:

```bash
npm start
```

### Step 6: Open the Application

Open your browser and visit:

http://localhost:4200/

Enter a website URL, for example:

```text
https://example.com
```

Click the scan button to analyze the website's security headers and SSL certificate.

Use the AI explanation button to generate security recommendations in Arabic.

**Important:** Both the frontend and backend must be running simultaneously.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/hello` | Check backend availability |
| GET | `/api/scan` | Analyze security headers and SSL certificate |
| GET | `/api/explain` | Generate AI-powered security recommendations |

Example scan request:

```text
http://localhost:8000/api/scan?url=https://example.com
```

## How It Works

1. The user enters a website URL in the Angular application.
2. Angular sends a request to the FastAPI backend.
3. FastAPI retrieves the website's HTTP response.
4. The backend checks four security headers and the SSL certificate.
5. The scan results are displayed in the Angular interface.
6. The user can request an AI-generated Arabic security report through Groq.

## Limitations

- The application performs basic security checks, not a comprehensive penetration test.
- The presence of security headers does not guarantee complete website security.
- SSL verification depends on certificate validation and network connectivity.
- AI-generated recommendations should be independently reviewed.
- Additional URL validation, network access restrictions, and other security protections are necessary before deploying the backend publicly.

## Future Improvements

- Add more security header checks.
- Improve URL validation and error handling.
- Add scan history.
- Export security reports as PDF files.
- Add automated backend and frontend tests.

## Author

**Khadija Alalawi**

Software Engineering Graduate

Developed as a practical full-stack software engineering portfolio project.