import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

def summarize_code(code: str, model="llama3-70b-8192") -> str:
    system_prompt = """You are a senior software engineer and technical writer.

Your task is to analyze a code snippet written in a programming language like Python, JavaScript, or Java. 
You must generate a clear and detailed explanation of what the code does.

Please include:
1. A **high-level summary** of the code
2. A **step-by-step breakdown** of how the code works
3. **Inline explanations** if the logic is tricky
4. A simple, hypothetical **example input and output** if applicable
5. The purpose or utility of this code (what problem it solves)

Use beginner-friendly language, but don’t skip technical accuracy.

Format the response clearly using sections like: Summary, Step-by-step, Example, Use Case.
"""

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": code}
        ],
        temperature=0.4,
        max_tokens=1024,
    )
    return response.choices[0].message.content.strip()
