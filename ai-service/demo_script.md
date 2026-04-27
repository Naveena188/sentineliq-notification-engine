# AI Demo Script — Day 14
## SentinelIQ Notification Engine
## AI Developer 1: Naveena S

---

## Demo Day Presentation (6 minutes total)

### Opening (1 minute)
"Our project is the SentinelIQ Notification Engine.
It uses AI to automatically describe, analyze and generate
reports for system notification events.
Let me show you the live system."

---

### AI Features Demo (2 minutes)

#### Step 1 — Show /health endpoint
URL: http://localhost:5000/health
Say: "This is our AI service health endpoint.
It shows the model we are using — LLaMA 3.3-70b,
uptime, and all available endpoints."

#### Step 2 — Show /describe endpoint
Input: "Server CPU usage exceeded 90%"
Say: "When a notification event occurs, our AI
automatically describes it professionally with
title, severity and recommended actions."

#### Step 3 — Show /recommend endpoint
Input: "Database connection failed"
Say: "Our AI also gives 3 actionable recommendations
for each event — each with action type and priority level."

#### Step 4 — Show /generate-report endpoint
Input: "Payment transaction failed"
Say: "Finally, our AI can generate a full structured
report with title, summary, overview, key items
and recommendations — all automatically!"

---

### Tech Explanation (1 minute)
"Our AI service is built with:
- Python Flask running on port 5000
- Groq API with LLaMA 3.3-70b model
- In-memory caching with SHA256 keys
- Security headers on all responses
- Input validation on all endpoints"

---

### Security Features (30 seconds)
"We have implemented:
- Input validation — returns 400 for empty input
- Security headers — X-Frame-Options, XSS Protection
- API key protection via .env file
- Prompt injection protection"

---

### Q&A Answers

Q: What does your AI service do?
A: "It automatically describes notification events,
provides recommendations, and generates full reports
using the LLaMA AI model via Groq API."

Q: What AI model are you using?
A: "We are using LLaMA 3.3-70b-versatile model
accessed through the Groq API which is free tier."

Q: What security measures did you implement?
A: "We added 7 security headers, input validation
on all endpoints, API key protection, and
prompt injection resistance."

Q: What happens if the AI fails?
A: "We have fallback responses with is_fallback: true
so the service never crashes even if Groq is down."

---

## Response Times (Record These)
- /health: ___ seconds
- /describe: ___ seconds
- /recommend: ___ seconds
- /generate-report: ___ seconds

## Backup Screenshots Needed
1. /health response screenshot
2. /describe response screenshot
3. /recommend response screenshot
4. /generate-report response screenshot