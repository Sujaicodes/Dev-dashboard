import requests
from datetime import datetime

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

news_url = f"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey={NEWS_API_KEY}"

news_response = requests.get(news_url)
news_data = news_response.json()

articles = news_data["articles"][:5]

news_list = ""
for article in articles:
    title = article["title"]
    news_list += f"- {title}\n"
    
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

## ⚡ About
Auto-updated using Python + GitHub Actions
"""

with open("README.md", "w") as f:
    f.write(content)
