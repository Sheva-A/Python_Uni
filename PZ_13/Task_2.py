# Програма читає текстовий файл і підраховує кількість рядків, слів та символів

filename = input("Введіть назву файлу для аналізу (з .txt): ")

# Ініціалізація лічильників
lines_count = 0
words_count = 0
chars_count = 0

# Читання файлу та підрахунок
with open(filename, 'r', encoding='utf-8') as file:
    for line in file:
        lines_count += 1
        words_count += len(line.split())
        chars_count += len(line)

# Виведення результатів
print("\nАналіз вмісту файлу:")
print(f"Кількість рядків:   {lines_count}")
print(f"Кількість слів:     {words_count}")
print(f"Кількість символів: {chars_count}")
