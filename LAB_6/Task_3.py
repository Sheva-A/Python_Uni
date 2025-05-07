import random  # Імпортуємо модуль для випадкових значень

# Список можливих варіантів
options = ["камінь", "ножиці", "папір", "ящірка", "спок"]

print("Гра 'Камінь-ножиці-папір-ящірка-Спок'!")
print("Варіанти: камінь, ножиці, папір, ящірка, спок")

try:
    # Отримуємо вибір гравця
    player_choice = input("Ваш вибір: ").strip().lower()

    # Якщо вибір неправильний — викликаємо помилку
    if player_choice not in options:
        raise ValueError("Некоректний вибір! Спробуйте ще раз.")

    # Комп’ютер обирає випадково
    computer_choice = random.choice(options)
    print(f"Комп'ютер обрав: {computer_choice}")

    # Перевірка результату гри
    if player_choice == computer_choice:
        print("Нічия!")
    elif player_choice == "камінь" and (computer_choice == "ножиці" or computer_choice == "ящірка"):
        print("Ви перемогли!")
    elif player_choice == "ножиці" and (computer_choice == "папір" or computer_choice == "ящірка"):
        print("Ви перемогли!")
    elif player_choice == "папір" and (computer_choice == "камінь" or computer_choice == "спок"):
        print("Ви перемогли!")
    elif player_choice == "ящірка" and (computer_choice == "папір" or computer_choice == "спок"):
        print("Ви перемогли!")
    elif player_choice == "спок" and (computer_choice == "ножиці" or computer_choice == "камінь"):
        print("Ви перемогли!")
    else:
        print("Комп'ютер переміг!")

# Якщо ввели щось некоректне
except ValueError:
    print("Некоректний вибір! Спробуйте ще раз.")

# Завершення гри
print("Дякуємо за гру!")