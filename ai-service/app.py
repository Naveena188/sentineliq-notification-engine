from flask import Flask
from dotenv import load_dotenv
import os
import time

load_dotenv()

app = Flask(__name__)

# Track server start time
START_TIME = time.time()

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