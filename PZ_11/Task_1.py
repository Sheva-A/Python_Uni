"""
Виведення високих оцінок зі списку.
Використовується генератор списку для фільтрації оцінок > 70.
"""

scores = [85, 60, 90, 70, 55, 100, 40, 78]
high_scores = [score for score in scores if score > 70]

print("Високі оцінки:", high_scores)
print("Кількість високих оцінок:", len(high_scores))
