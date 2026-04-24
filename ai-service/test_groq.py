import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def test_prompt(input_text):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": f"You are a helpful assistant for a notification engine system. Describe the following item clearly and professionally. Item: {input_text}"
            }
        ],
        temperature=0.3,
        max_tokens=200
    )
    return response.choices[0].message.content

# Test with 5 inputs
test_inputs = [
    "Server CPU usage exceeded 90%",
    "New user registered successfully",
    "Payment transaction failed",
    "Database backup completed",
    "API response time is slow"
]

for i, input_text in enumerate(test_inputs, 1):
    print(f"\n--- Test {i} ---")
    print(f"Input: {input_text}")
    print(f"Output: {test_prompt(input_text)}")