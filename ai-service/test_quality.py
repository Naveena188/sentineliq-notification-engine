import os
import sys
from dotenv import load_dotenv

load_dotenv()

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from services.groq_client import get_description, get_recommendations, get_report

# 10 test inputs
test_inputs = [
    "Server CPU usage exceeded 90%",
    "Database connection failed",
    "Payment transaction declined",
    "New user registration successful",
    "API response time exceeded 5 seconds",
    "Memory usage critical - 95% used",
    "File upload completed successfully",
    "Authentication failed - invalid token",
    "Scheduled backup completed",
    "Network connectivity lost"
]

print("=" * 60)
print("AI QUALITY TEST - DAY 10")
print("=" * 60)

# Test /describe endpoint
print("\n--- Testing /describe endpoint ---")
describe_scores = []
for i, input_text in enumerate(test_inputs, 1):
    print(f"\nTest {i}: {input_text}")
    result = get_description(input_text)
    print(f"Output: {result[:100]}...")
    score = 4 if len(result) > 50 else 2
    describe_scores.append(score)
    print(f"Score: {score}/5")

avg_describe = sum(describe_scores) / len(describe_scores)
print(f"\n/describe Average Score: {avg_describe}/5")

# Test /recommend endpoint
print("\n--- Testing /recommend endpoint ---")
recommend_scores = []
for i, input_text in enumerate(test_inputs, 1):
    print(f"\nTest {i}: {input_text}")
    result = get_recommendations(input_text)
    print(f"Output: {result}")
    score = 4 if len(result) == 3 else 2
    recommend_scores.append(score)
    print(f"Score: {score}/5")

avg_recommend = sum(recommend_scores) / len(recommend_scores)
print(f"\n/recommend Average Score: {avg_recommend}/5")

# Test /generate-report endpoint
print("\n--- Testing /generate-report endpoint ---")
report_scores = []
for i, input_text in enumerate(test_inputs, 1):
    print(f"\nTest {i}: {input_text}")
    result = get_report(input_text)
    print(f"Output keys: {list(result.keys())}")
    score = 4 if 'title' in result and 'summary' in result else 2
    report_scores.append(score)
    print(f"Score: {score}/5")

avg_report = sum(report_scores) / len(report_scores)
print(f"\n/generate-report Average Score: {avg_report}/5")

print("\n" + "=" * 60)
print("FINAL RESULTS")
print("=" * 60)
print(f"/describe avg score: {avg_describe}/5")
print(f"/recommend avg score: {avg_recommend}/5")
print(f"/generate-report avg score: {avg_report}/5")
overall = (avg_describe + avg_recommend + avg_report) / 3
print(f"Overall avg score: {overall}/5")
if overall >= 4:
    print("RESULT: PASS - All endpoints meeting quality target!")
else:
    print("RESULT: NEEDS IMPROVEMENT")
print("=" * 60)