# assistant/gpt_assistant.py
import os
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv

# Load .env variables (optional)
load_dotenv()

# Setup OpenRouter client
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)

def generate_summary(df: pd.DataFrame) -> str:
    content = "Here is my recent app usage log:\n\n"
    content += df.to_string(index=False)
    content += "\n\nPlease give a short productivity summary and suggestions for improvement."

    try:
        response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",  # Or try other models like "mistralai/mistral-7b-instruct"
            messages=[
                {"role": "system", "content": "You are a productivity assistant."},
                {"role": "user", "content": content}
            ]
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"⚠️ GPT Error: {str(e)}"
