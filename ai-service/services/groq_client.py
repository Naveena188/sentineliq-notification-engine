import os
import json
import hashlib
import time
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Simple in-memory cache (replaces Redis for now)
cache = {}
CACHE_TTL = 900  # 15 minutes in seconds

def get_cache_key(prompt_file, input_text):
    raw = f"{prompt_file}:{input_text}"
    return hashlib.sha256(raw.encode()).hexdigest()

def get_from_cache(key):
    if key in cache:
        entry = cache[key]
        if time.time() - entry['timestamp'] < CACHE_TTL:
            print(f"Cache HIT for key: {key[:20]}...")
            return entry['value']
        else:
            del cache[key]
    return None

def save_to_cache(key, value):
    cache[key] = {
        'value': value,
        'timestamp': time.time()
    }
    print(f"Cache SAVED for key: {key[:20]}...")

def load_prompt(prompt_file):
    prompt_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        'prompts',
        prompt_file
    )
    with open(prompt_path, 'r') as f:
        return f.read()

def get_description(input_text):
    try:
        cache_key = get_cache_key('describe', input_text)
        cached = get_from_cache(cache_key)
        if cached:
            return cached

        prompt_template = load_prompt('describe_prompt.txt')
        prompt = prompt_template.replace('{input}', input_text)
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=300
        )
        result = response.choices[0].message.content
        save_to_cache(cache_key, result)
        return result
    except Exception as e:
        return f"AI service error: {str(e)}"

def get_recommendations(input_text):
    try:
        cache_key = get_cache_key('recommend', input_text)
        cached = get_from_cache(cache_key)
        if cached:
            return cached

        prompt_template = load_prompt('recommend_prompt.txt')
        prompt = prompt_template.replace('{input}', input_text)
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=500
        )
        content = response.choices[0].message.content
        recommendations = json.loads(content)
        save_to_cache(cache_key, recommendations)
        return recommendations
    except json.JSONDecodeError:
        return [
            {"action_type": "ALERT", "description": "Review the notification event immediately", "priority": "HIGH"},
            {"action_type": "INVESTIGATE", "description": "Check system logs for more details", "priority": "MEDIUM"},
            {"action_type": "MONITOR", "description": "Monitor system for next 30 minutes", "priority": "LOW"}
        ]
    except Exception as e:
        return [{"action_type": "ERROR", "description": str(e), "priority": "HIGH"}]

def get_report(input_text):
    try:
        cache_key = get_cache_key('report', input_text)
        cached = get_from_cache(cache_key)
        if cached:
            return cached

        prompt_template = load_prompt('report_prompt.txt')
        prompt = prompt_template.replace('{input}', input_text)
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=1000
        )
        content = response.choices[0].message.content
        report = json.loads(content)
        save_to_cache(cache_key, report)
        return report
    except json.JSONDecodeError:
        return {
            "title": "Report Generation Error",
            "summary": "Unable to generate report at this time.",
            "overview": "The AI service encountered an error while generating the report.",
            "key_items": ["Service temporarily unavailable"],
            "recommendations": [
                {"action": "Retry the request", "priority": "HIGH"}
            ],
            "is_fallback": True
        }
    except Exception as e:
        return {
            "title": "Error",
            "summary": str(e),
            "overview": "An error occurred",
            "key_items": [],
            "recommendations": [],
            "is_fallback": True
        }