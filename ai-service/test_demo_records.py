import os
import sys
from dotenv import load_dotenv

load_dotenv()

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from services.groq_client import get_description, get_recommendations

# 30 demo records
demo_records = [
    "Server CPU usage exceeded 90%",
    "Database connection failed",
    "Payment transaction declined",
    "New user registration successful",
    "API response time exceeded 5 seconds",
    "Memory usage critical - 95% used",
    "File upload completed successfully",
    "Authentication failed - invalid token",
    "Scheduled backup completed",
    "Network connectivity lost",
    "Disk space usage at 85%",
    "Email notification sent successfully",
    "SSL certificate expiring in 7 days",
    "Service restart completed successfully",
    "Login attempt from unknown IP address",
    "Database query taking more than 10 seconds",
    "Cache memory cleared successfully",
    "New order placed successfully",
    "System update installed successfully",
    "User password reset requested",
    "API rate limit exceeded",
    "Server response time normal",
    "Backup storage almost full",
    "User account locked after failed attempts",
    "Third party service unavailable",
    "Data export completed successfully",
    "Security scan completed - no threats found",
    "Load balancer health check failed",
    "Mobile app crash reported",
    "Monthly report generated successfully"
]

print("=" * 60)
print("DEMO RECORDS TEST - DAY 12")
print("=" * 60)
print(f"Testing {len(demo_records)} demo records...")

passed = 0
failed = 0

for i, record in enumerate(demo_records, 1):
    print(f"\nRecord {i}: {record}")
    try:
        description = get_description(record)
        if description and len(description) > 20:
            print(f"✅ Description: OK ({len(description)} chars)")
            passed += 1
        else:
            print(f"❌ Description: FAILED")
            failed += 1
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        failed += 1

print("\n" + "=" * 60)
print("RESULTS")
print("=" * 60)
print(f"Total records: {len(demo_records)}")
print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"Success rate: {(passed/len(demo_records))*100:.1f}%")
if passed == len(demo_records):
    print("ALL DEMO RECORDS READY! ✅")
else:
    print("Some records need attention!")
print("=" * 60)