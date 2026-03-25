import requests
from datetime import datetime

from groq import Groq
import os

groq_key = os.getenv("GROQ_API_KEY")

ai_output = "AI insight not available."

if groq_key:
    try:
        client = Groq(api_key=groq_key)

        news_text = "\n".join([article.get("title", "") for article in articles])

        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "Summarize the news and give one short insight."},
                {"role": "user", "content": news_text}
            ]
        )

        ai_output = response.choices[0].message.content

    except Exception as e:
        ai_output = f"Error generating AI insight: {e}"
else:
    ai_output = "GROQ API key missing."



# ---- CONFIG ----
API_KEY = "b4194471d5254484872163149251206"
CITY = "Chennai"

# ---- WEATHER API ----
url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}"

response = requests.get(url)
data = response.json()

temp = data["current"]["temp_c"]
condition = data["current"]["condition"]["text"]

# ---- NEWS API ----
NEWS_API_KEY = "b3627940bba147568e4d150c345774e0"

news_url = f"https://newsapi.org/v2/everything?q=technology&language=en&sortBy=publishedAt&apiKey={NEWS_API_KEY}"

news_response = requests.get(news_url)
news_data = news_response.json()

news_list = ""
articles = []   # ✅ define globally

if news_data.get("status") == "ok" and news_data.get("articles"):
    articles = news_data["articles"][:5]

    for article in articles:
        title = article.get("title", "No title")
        news_list += f"- {title}\n"
else:
    news_list = "No news available right now."

print(news_data)
# ---- TIME ----
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# ---- README CONTENT ----
content = f"""
# 🚀 Sujai's Dev Dashboard

🕒 Last Updated: {now}

---

## 🌦️ Weather in {CITY}
Temperature: {temp}°C  
Condition: {condition}

---

## 📰 Top Tech News
{news_list if news_list else "No news available right now."}

---

## 🧠 AI Insight
{ai_output}

## ⚡ About
Auto-updated using Python + GitHub Actions
"""

with open("README.md", "w") as f:
    f.write(content)
