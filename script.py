import requests
from datetime import datetime
import os
from groq import Groq

# ---- CONFIG ----
CITY = "Chennai"
WEATHER_API_KEY = "b4194471d5254484872163149251206"
NEWS_API_KEY = os.getenv("NEWS_API_KEY") or "b3627940bba147568e4d150c345774e0"
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ---- WEATHER ----
weather_url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={CITY}"
weather_data = requests.get(weather_url).json()

temp = weather_data["current"]["temp_c"]
condition = weather_data["current"]["condition"]["text"]

# ---- NEWS ----
news_url = f"https://newsapi.org/v2/everything?q=technology&language=en&sortBy=publishedAt&apiKey={NEWS_API_KEY}"
news_data = requests.get(news_url).json()

articles = []  # ✅ ALWAYS defined

news_list = ""

if news_data.get("status") == "ok" and news_data.get("articles"):
    articles = news_data["articles"][:5]

    for article in articles:
        title = article.get("title", "No title")
        news_list += f"- {title}\n"
else:
    news_list = "No news available right now."

# ---- AI (GROQ) ----
ai_output = "AI insight not available."

if GROQ_API_KEY:
    try:
        client = Groq(api_key=GROQ_API_KEY)

        news_text = "\n".join([article.get("title", "") for article in articles])

        if news_text.strip():  # only if news exists
            response = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {"role": "system", "content": "Summarize the news and give one short insight."},
                    {"role": "user", "content": news_text}
                ]
            )

            ai_output = response.choices[0].message.content
        else:
            ai_output = "No news available for AI analysis."

    except Exception as e:
        ai_output = f"Error generating AI insight: {e}"
else:
    ai_output = "GROQ API key missing."

# ---- TIME ----
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# ---- README ----
content = f"""
# 🚀 Sujai's Dev Dashboard

🕒 Last Updated: {now}

---

## 🌦️ Weather in {CITY}
Temperature: {temp}°C  
Condition: {condition}

---

## 📰 Top Tech News
{news_list}

---

## 🧠 AI Insight
{ai_output}

---

## ⚡ About
Auto-updated using Python + GitHub Actions + AI
"""

with open("README.md", "w") as f:
    f.write(content)
