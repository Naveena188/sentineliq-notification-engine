from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import time

load_dotenv()

app = Flask(__name__)

# Track server start time
START_TIME = time.time()

# Security Headers Middleware
@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate'
    return response

# Register blueprints
from routes.describe import describe_bp
from routes.recommend import recommend_bp
from routes.generate_report import generate_report_bp

app.register_blueprint(describe_bp)
app.register_blueprint(recommend_bp)
app.register_blueprint(generate_report_bp)

@app.route("/health", methods=["GET"])
def health():
    uptime_seconds = int(time.time() - START_TIME)
    uptime_minutes = uptime_seconds // 60
    uptime_hours = uptime_minutes // 60

    return {
        "status": "ok",
        "model": "llama-3.3-70b-versatile",
        "message": "AI service is running",
        "uptime": {
            "seconds": uptime_seconds,
            "minutes": uptime_minutes,
            "hours": uptime_hours
        },
        "endpoints": [
            "/health",
            "/describe",
            "/recommend",
            "/generate-report"
        ],
        "version": "1.0.0"
    }, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)