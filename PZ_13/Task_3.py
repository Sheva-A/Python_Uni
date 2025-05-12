"""
Програма виконує пошук і заміну вмісту текстового файлу,
зберігає результат у новому файлі
"""

filename = input("Введіть назву файлу для редагування (з .txt): ")
search_text = input("Введіть слово або фразу для пошуку: ")
replace_text = input("Введіть слово або фразу для заміни: ")
new_filename = input("Введіть назву нового файлу для збереження (з .txt): ")

# Зчитування вмісту оригінального файлу
with open(filename, 'r', encoding='utf-8') as file:
    content = file.read()

# Замінюємо шукане слово/фразу
new_content = content.replace(search_text, replace_text)

# Запис результату в новий файл
with open(new_filename, 'w', encoding='utf-8') as file:
    file.write(new_content)

print("\nЗаміна виконана. Результат збережено у файлі:", new_filename)
