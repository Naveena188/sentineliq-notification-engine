from flask import Blueprint, request, jsonify
from datetime import datetime, timezone
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from services.groq_client import get_report

generate_report_bp = Blueprint('generate_report', __name__)

@generate_report_bp.route('/generate-report', methods=['POST'])
def generate_report():
    data = request.get_json()

    # Validate input
    if not data or 'input' not in data:
        return jsonify({
            "success": False,
            "error": "input field is required"
        }), 400

    input_text = data['input'].strip()

    if not input_text:
        return jsonify({
            "success": False,
            "error": "input cannot be empty"
        }), 400

    # Call Groq AI
    report = get_report(input_text)

    return jsonify({
        "success": True,
        "input": input_text,
        "report": report,
        "generated_at": datetime.now(timezone.utc).isoformat()
    }), 200