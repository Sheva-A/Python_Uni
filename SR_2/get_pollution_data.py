import json
import time
import requests

API_KEY = "b8a8c9ff-0fd2-49c8-9847-42dbe5a4b2d2"
BASE_URL = "http://api.airvisual.com/v2/city"

with open("ukrainian_cities.json", "r", encoding="utf-8") as file:
    cities = json.load(file)

results = []

for city in cities:
    params = {
        "city": city["city"],
        "state": city["state"],
        "country": city["country"],
        "key": API_KEY
    }

    for attempt in range(6):
        try:
            response = requests.get(BASE_URL, params=params, timeout=10)
            if response.status_code == 429:
                print(f"[{city['city']}] Забагато запитів. Повтор через 15 с…")
                time.sleep(15)
                continue

            data = response.json()
            if data.get("status") == "success":
                pollution = data["data"]["current"]["pollution"]
                results.append({
                    "city": city["city"],
                    "state": city["state"],
                    "country": city["country"],
                    "aqius": pollution["aqius"]
                })
            else:
                print(f"[{city['city']}] API помилка: {data.get('data')}")
            break
        except Exception as e:
            print(f"[{city['city']}] Виняток: {e}")
            break

    time.sleep(10)

with open("pollution_results.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("Дані збережено у pollution_results.json")










