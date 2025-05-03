"""
Пошук чисел, що повторюються у списку.
Використовуються тільки цикли та умовні оператори.
"""

numbers = [1, 2, 3, 4, 3, 2, 5, 6, 5, 7]
duplicates = []

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print("Повторювані числа:", duplicates)
