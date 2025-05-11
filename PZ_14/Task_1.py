import json
import os

STATS_FILE = 'game_stats.json'

def load_stats():
    if os.path.exists(STATS_FILE):
        with open(STATS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_stats(stats):
    with open(STATS_FILE, 'w', encoding='utf-8') as f:
        json.dump(stats, f, ensure_ascii=False, indent=4)

def update_stats(player_name, result):
    stats = load_stats()
    if player_name not in stats:
        stats[player_name] = {"games": 0, "wins": 0}
    stats[player_name]["games"] += 1
    if result == "win":
        stats[player_name]["wins"] += 1
    save_stats(stats)


update_stats("Іван", "win")
update_stats("Іван", "lose")

update_stats("Макс", "lose")
update_stats("Макс", "lose")
update_stats("Макс", "win")

print(load_stats())
