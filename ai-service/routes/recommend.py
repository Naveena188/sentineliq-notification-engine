from flask import Blueprint, request, jsonify
from datetime import datetime, timezone
import os
import sys
import json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from services.groq_client import get_recommendations

recommend_bp = Blueprint('recommend', __name__)

@recommend_bp.route('/recommend', methods=['POST'])
def recommend():
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
    recommendations = get_recommendations(input_text)

    return jsonify({
        "success": True,
        "input": input_text,
        "recommendations": recommendations,
        "generated_at": datetime.now(timezone.utc).isoformat()
    }), 200