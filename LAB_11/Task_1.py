phonebook = [
    {"ім'я": "Анна", "прізвище": "Іванова", "телефон": "0501234567", "місто": "Київ"},
    {"ім'я": "Олег", "прізвище": "Петренко", "телефон": "0667654321", "місто": "Львів"},
    {"ім'я": "Марія", "прізвище": "Коваль", "телефон": "0731112233", "місто": "Київ"},
    {"ім'я": "Іван", "прізвище": "Сидоренко", "телефон": "0673334445", "місто": "Одеса"},
    {"ім'я": "Наталя", "прізвище": "Бондаренко", "телефон": "0995556677", "місто": "Харків"}
]

def show_contacts():
    print(f"{'Ім\'я':<10}{'Прізвище':<15}{'Телефон':<15}{'Місто':<10}")
    print("-" * 50)
    for contact in phonebook:
        print(f"{contact['ім\'я']:<10}{contact['прізвище']:<15}{contact['телефон']:<15}{contact['місто']:<10}")
    print()

def search_contacts():
    try:
        criteria = input("Введіть параметр пошуку (ім'я / прізвище / місто): ").strip().lower()
        if criteria not in ["ім'я", "прізвище", "місто"]:
            raise ValueError("Некоректний параметр пошуку.")
        query = input(f"Введіть значення для {criteria}: ").strip()
        if not query:
            raise ValueError("Порожній запит.")
        found = [c for c in phonebook if c[criteria].lower() == query.lower()]
        if found:
            print("Знайдені контакти:")
            print(f"{'Ім\'я':<10}{'Прізвище':<15}{'Телефон':<15}{'Місто':<10}")
            print("-" * 50)
            for c in found:
                print(f"{c['ім\'я']:<10}{c['прізвище']:<15}{c['телефон']:<15}{c['місто']:<10}")
        else:
            print("Контакти не знайдено.")
    except ValueError as e:
        print("Помилка:", e)
    print()

def update_or_delete_contact():
    try:
        surname = input("Введіть прізвище контакту для оновлення або видалення: ").strip()
        matches = [c for c in phonebook if c["прізвище"].lower() == surname.lower()]
        if not matches:
            print("Контакт не знайдено.")
            return
        contact = matches[0]
        print("Знайдено контакт:")
        print(contact)

        action = input("Бажаєте оновити чи видалити? (оновити/видалити): ").strip().lower()
        if action == "оновити":
            contact["ім'я"] = input("Нове ім'я: ").strip() or contact["ім'я"]
            contact["прізвище"] = input("Нове прізвище: ").strip() or contact["прізвище"]
            contact["телефон"] = input("Новий телефон: ").strip() or contact["телефон"]
            contact["місто"] = input("Нове місто: ").strip() or contact["місто"]
            print("Контакт оновлено.")
        elif action == "видалити":
            phonebook.remove(contact)
            print("Контакт видалено.")
        else:
            print("Невідома дія.")
    except Exception as e:
        print("Помилка:", e)
    print()

def analytics():
    cities = {c['місто'] for c in phonebook}
    print("Унікальні міста:", cities)

    city_count = {}
    for contact in phonebook:
        city = contact['місто']
        city_count[city] = city_count.get(city, 0) + 1

    print("\nКількість контактів по містах:")
    for city, count in city_count.items():
        print(f"{city}: {count}")

    if city_count:
        max_city = max(city_count, key=city_count.get)
        print(f"\nМісто з найбільшою кількістю контактів: {max_city}")
    print()

def main():
    while True:
        print("1. Показати всі контакти")
        print("2. Пошук контакту")
        print("3. Оновлення або видалення контакту")
        print("4. Аналітика")
        print("5. Вихід")
        choice = input("Оберіть опцію: ").strip()

        if choice == '1':
            show_contacts()
        elif choice == '2':
            search_contacts()
        elif choice == '3':
            update_or_delete_contact()
        elif choice == '4':
            analytics()
        elif choice == '5':
            break
        else:
            print("Невірна опція. Спробуйте ще раз.\n")

if __name__ == "__main__":
    main()
