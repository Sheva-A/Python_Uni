"""
Програма створює новий файл, дозволяє вводити кілька рядків тексту,
виводить вміст файлу після збереження
"""

filename = input("Введіть назву нового файлу (з .txt): ")

# Відкриваємо файл для запису (створюється новий або перезаписується)
with open(filename, 'w', encoding='utf-8') as file:
    print("Вводьте текст (порожній рядок — завершити):")
    while True:
        line = input()
        if line == "":
            break
        file.write(line + '\n')

# Відкриваємо файл для читання та виводимо його вміст
print("\nВміст файлу:")
with open(filename, 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)
