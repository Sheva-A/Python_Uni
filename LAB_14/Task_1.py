import os

FILENAME = "travel_diary.txt"

def add_entry():
    date = input("Введіть дату (рррр-мм-дд): ")
    location = input("Введіть локацію: ")
    text = input("Введіть текст запису: ")

    with open(FILENAME, "a", encoding="utf-8") as file:
        file.write(f"Дата: {date}\n")
        file.write(f"Локація: {location}\n")
        file.write(f"Текст: {text}\n")
        file.write("===\n")
    print("Запис додано.\n")

def search_entries():
    query = input("Введіть дату або ключове слово для пошуку: ").lower()
    if not os.path.exists(FILENAME):
        print("Файл щоденника ще не створено.")
        return

    with open(FILENAME, "r", encoding="utf-8") as file:
        entries = file.read().split("===\n")

    found = False
    for entry in entries:
        if query in entry.lower():
            print(entry.strip())
            print("---")
            found = True

    if not found:
        print("Записи не знайдено.\n")

def analytics():
    if not os.path.exists(FILENAME):
        print("Файл щоденника ще не створено.")
        return

    with open(FILENAME, "r", encoding="utf-8") as file:
        entries = file.read().split("===\n")

    entries = [entry for entry in entries if entry.strip()]
    total_entries = len(entries)
    locations = set()
    word_count = 0

    for entry in entries:
        lines = entry.strip().split("\n")
        for line in lines:
            if line.startswith("Локація: "):
                location = line.replace("Локація: ", "").strip()
                locations.add(location)
            if line.startswith("Текст: "):
                text = line.replace("Текст: ", "").strip()
                word_count += len(text.split())

    print(f"Кількість записів: {total_entries}")
    print(f"Кількість відвіданих локацій: {len(locations)}")
    print(f"Загальна кількість слів у записах: {word_count}\n")

def main():
    while True:
        print("1. Додати запис")
        print("2. Пошук записів")
        print("3. Аналітика подорожей")
        print("4. Вихід")
        choice = input("Оберіть опцію: ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            search_entries()
        elif choice == "3":
            analytics()
        elif choice == "4":
            break
        else:
            print("Невірний вибір.\n")

if __name__ == "__main__":
    main()
