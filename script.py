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
