import requests
from datetime import datetime

# ---- CONFIG ----
CITY = "Chennai"

# ---- WEATHER (dummy for now, we upgrade later) ----
weather = "Sunny ☀️"

# ---- TIME ----
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# ---- CONTENT ----
content = f"""
# 🚀 Sujai's Dev Dashboard

🕒 Last Updated: {now}

---

## 🌦️ Weather in {CITY}
{weather}

---

## 🧠 Daily Insight
"Stay consistent. Small steps every day = big results."

---

## ⚡ About This Project
Built an automated developer dashboard using Python and GitHub Actions that fetches real-time data and updates dynamically on a daily schedule.
---
"""

with open("README.md", "w") as f:
    f.write(content)