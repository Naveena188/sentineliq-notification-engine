# Demo Day Rehearsal Notes
## AI Developer 1: Naveena S
## Rehearsal 2 — Day 17

---

## 6-Minute Presentation Plan

### Opening (1 minute)
- State the problem in one sentence
- Show architecture
- Say "Let me show you the live tool"

### AI Demo (3 minutes)

#### 1. Show /health (30 seconds)
URL: http://localhost:5000/health
Points to mention:
- Model: llama-3.3-70b-versatile
- Uptime tracking
- All 4 endpoints listed

#### 2. Show /describe (1 minute)
Input: "Server CPU usage exceeded 90%"
Points to mention:
- AI describes notification professionally
- Returns structured JSON
- Has generated_at timestamp

#### 3. Show /recommend (1 minute)
Input: "Database connection failed"
Points to mention:
- Returns exactly 3 recommendations
- Each has action_type, description, priority
- Priority levels: LOW, MEDIUM, HIGH, CRITICAL

#### 4. Show /generate-report (30 seconds)
Input: "Payment transaction failed"
Points to mention:
- Full structured report
- Has title, summary, overview
- Has key_items and recommendations

### Tech Explanation (1 minute)
- Python Flask on port 5000
- Groq API with LLaMA 3.3-70b
- In-memory caching SHA256 keys
- Security headers on all responses

### Security Demo (30 seconds)
- Show 400 on empty input
- Mention security headers
- Reference SECURITY.md

### Q&A (30 seconds)

---

## 5 Key Questions and Answers

### Q1: What does your AI service do?
"Our AI service automatically analyzes notification
events. It can describe them professionally, give
3 actionable recommendations, and generate full
structured reports — all powered by LLaMA AI."

### Q2: What AI model are you using?
"We use LLaMA 3.3-70b-versatile model accessed
through the Groq API which provides free tier
access with fast response times."

### Q3: What happens if the AI is unavailable?
"We have fallback responses built in. If Groq API
fails, our service returns a default response with
is_fallback: true so the service never crashes."

### Q4: What security measures did you implement?
"We implemented 7 security headers including
X-Frame-Options, XSS Protection and Content
Security Policy. We also have input validation
on all endpoints and API key protection."

### Q5: How fast are your endpoints?
"Our endpoints respond in 1-3 seconds on average.
We also implemented caching with SHA256 keys
and 15 minute TTL so repeated requests are
instant."

---

## Rehearsal Checklist
- [ ] Server starts correctly ✅
- [ ] /health endpoint working ✅
- [ ] /describe endpoint working ✅
- [ ] /recommend endpoint working ✅
- [ ] /generate-report endpoint working ✅
- [ ] Can answer all 5 questions without notes ✅
- [ ] Demo fits in 6 minutes ✅
- [ ] Browser ready with localhost:5000/health ✅

---

## Issues Found in Rehearsal
None - All endpoints working correctly!

## Sign-off
- AI Developer 1: Naveena S ✅
- Date: 27 April 2026
- Status: READY FOR DEMO DAY ✅