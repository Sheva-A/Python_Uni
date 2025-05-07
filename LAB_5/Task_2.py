import random  # Імпортуємо модуль random

the_number = random.randint(1, 50)  # Генеруємо випадкове число

while True:  # Нескінченний цикл, який триває, поки користувач не вгадає число
    try:
        user_number = int(input("Enter a number (1-50): "))  # Отримуємо число від користувача
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue  # Якщо введене значення не є числом, повторюємо введення

    if 1 <= user_number <= 50:  # Перевіряємо, чи входить число в потрібний діапазон
        difference = abs(the_number - user_number)
        if difference > 10:
            print("Far.")  # Якщо число більше ніж за десять позицій від загаданого
        elif 3 < difference <= 10:
            print("Close.")  # Якщо число більше ніж за 3 позиції
        elif 1 < difference <= 3:
            print("Very close!")  # Якщо число менше ніж за 3 позиції
        else:
            print("Congratulations! You guessed the number.")  # Користувач вгадав число
            print("Great game!")
            break  # Завершуємо гру
    else:
        print("Your number is not valid. Try again.")  # Число не входить у діапазон
