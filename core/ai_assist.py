import os
import openai
import asyncio

openai.api_key = os.getenv("OPENAI_API_KEY")

async def analyze(endpoints):
    prompt = "You are a cybersecurity expert. Analyze the following API endpoints and suggest potential abuse or vulnerabilities:\n\n"
    for ep in endpoints:
        prompt += f"- {ep['method']} {ep['path']}\n"

    prompt += "\nProvide concise, actionable advice."

    try:
        response = await openai.ChatCompletion.acreate(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful security assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.2,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"AI analysis error: {e}"

