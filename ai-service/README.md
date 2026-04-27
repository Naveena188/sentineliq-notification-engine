# AI Service — SentinelIQ Notification Engine

## Overview
This is the AI microservice for the SentinelIQ Notification Engine.
It uses Flask and Groq LLaMA 3.3-70b to provide AI-powered notification analysis.

## Tech Stack
- Python 3.11
- Flask 3.0.3
- Groq API (LLaMA-3.3-70b-versatile)
- flask-limiter
- flask-cors

## Prerequisites
- Python 3.11 installed
- Groq API key (free at console.groq.com)

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Naveena188/sentineliq-notification-engine.git
cd sentineliq-notification-engine/ai-service
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create .env file
```bash
cp .env.example .env
```
Add your Groq API key to .env:
GROQ_API_KEY=your_groq_api_key_here

### 4. Run the service
```bash
python app.py
```

### 5. Verify it's running
Open browser and go to:
http://localhost:5000/health

## API Reference

### GET /health
Returns service health status with uptime information.

**Response:**
```json
{
  "status": "ok",
  "model": "llama-3.3-70b-versatile",
  "message": "AI service is running",
  "uptime": {"seconds": 100, "minutes": 1, "hours": 0},
  "endpoints": ["/health", "/describe", "/recommend", "/generate-report"],
  "version": "1.0.0"
}
```

### POST /describe
Describes a notification event professionally.

**Request:**
```json
{"input": "Server CPU usage exceeded 90%"}
```

**Response:**
```json
{
  "success": true,
  "input": "Server CPU usage exceeded 90%",
  "description": "AI generated description...",
  "generated_at": "2026-04-26T..."
}
```

### POST /recommend
Returns 3 actionable recommendations for a notification event.

**Request:**
```json
{"input": "Server CPU usage exceeded 90%"}
```

**Response:**
```json
{
  "success": true,
  "input": "Server CPU usage exceeded 90%",
  "recommendations": [
    {"action_type": "ALERT", "description": "...", "priority": "HIGH"},
    {"action_type": "INVESTIGATE", "description": "...", "priority": "MEDIUM"},
    {"action_type": "MONITOR", "description": "...", "priority": "LOW"}
  ],
  "generated_at": "2026-04-26T..."
}
```

### POST /generate-report
Generates a full structured report for a notification event.

**Request:**
```json
{"input": "Server CPU usage exceeded 90%"}
```

**Response:**
```json
{
  "success": true,
  "input": "Server CPU usage exceeded 90%",
  "report": {
    "title": "Report Title",
    "summary": "Executive summary...",
    "overview": "Detailed overview...",
    "key_items": ["Point 1", "Point 2"],
    "recommendations": [
      {"action": "Take action", "priority": "HIGH"}
    ]
  },
  "generated_at": "2026-04-26T..."
}
```

## Fallback Responses
If Groq AI is unavailable, all endpoints return fallback responses with `is_fallback: true`

## Environment Variables
| Variable | Description | Required |
|----------|-------------|----------|
| GROQ_API_KEY | Your Groq API key | Yes |

## Security
- All endpoints validate input
- Security headers added to all responses
- API key stored in .env (never committed to GitHub)
- See SECURITY.md for full security documentation

## Team
- AI Developer 1: Naveena S
- Sprint: 14 April - 9 May 2026
## Docker Setup

### Build the Docker image
```bash
docker build -t ai-service .
```

### Run with Docker
```bash
docker run -p 5000:5000 --env-file .env ai-service
```

### Run with Docker Compose
```bash
docker-compose up
```

## Folder Structure
```
ai-service/
├── routes/
│   ├── describe.py
│   ├── recommend.py
│   └── generate_report.py
├── services/
│   └── groq_client.py
├── prompts/
│   ├── describe_prompt.txt
│   ├── recommend_prompt.txt
│   └── report_prompt.txt
├── app.py
├── requirements.txt
├── Dockerfile
├── .env.example
├── .gitignore
├── README.md
└── SECURITY.md
```