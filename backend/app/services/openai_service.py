import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_metrics_with_openai(metrics: dict, question: str) -> str:
    prompt = f"""
You are a social media analytics expert.

Given the following data:
{metrics}

And this question: "{question}"

Respond concisely and insightfully.
"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You analyze social media metrics."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content
