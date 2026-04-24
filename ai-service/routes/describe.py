from flask import Blueprint, request, jsonify
from datetime import datetime, timezone
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from services.groq_client import get_description

describe_bp = Blueprint('describe', __name__)

@describe_bp.route('/describe', methods=['POST'])
def describe():
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
    result = get_description(input_text)

    return jsonify({
        "success": True,
        "input": input_text,
        "description": result,
        "generated_at": datetime.now(timezone.utc).isoformat()
    }), 200