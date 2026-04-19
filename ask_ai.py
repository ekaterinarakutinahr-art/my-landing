import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")

api_key = os.getenv("OPENAI_API_KEY")
if not api_key or api_key == "sk-your-key-here":
    raise SystemExit("Ошибка: вставьте настоящий ключ в файл .env (OPENAI_API_KEY=sk-...)")

from openai import OpenAI

client = OpenAI(api_key=api_key)

prompt = (
    "Придумай 3 креативных названия для моего проекта: "
    "лендинг-страница для художника-иллюстратора, показывающая портфолио и принимающая заказы."
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
)

print(response.choices[0].message.content)
