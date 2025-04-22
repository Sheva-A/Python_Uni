import random


def main():
    options = ["камінь", "ножиці", "папір", "ящірка", "спок"]

    print("Гра 'Камінь-ножиці-папір-ящірка-Спок'!")
    print("Варіанти: камінь, ножиці, папір, ящірка, Спок")

    try:
        player_choice = input("Ваш вибір: ").strip().lower()

        if player_choice not in options:
            raise ValueError("Некоректний вибір! Спробуйте ще раз.")

        computer_choice = random.choice(options)
        print(f"Комп'ютер обрав: {computer_choice}")

        if player_choice == computer_choice:
            print("Нічия!")
        elif player_choice == "камінь" and (computer_choice == "ножиці" or computer_choice == "ящірка"):
            print("Ви перемогли!")
        elif player_choice == "ножиці" and (computer_choice == "папір" or computer_choice == "ящірка"):
            print("Ви перемогли!")
        elif player_choice == "папір" and (computer_choice == "камінь" or computer_choice == "Спок"):
            print("Ви перемогли!")
        elif player_choice == "ящірка" and (computer_choice == "папір" or computer_choice == "Спок"):
            print("Ви перемогли!")
        elif player_choice == "спок" and (computer_choice == "ножиці" or computer_choice == "камінь"):
            print("Ви перемогли!")
        else:
            print("Комп'ютер переміг!")

    except ValueError:
        print("Некоректний вибір! Спробуйте ще раз.")

    print("Дякуємо за гру!")


if __name__ == "__main__":
    main()