import random  # Імпортуємо модуль random

the_number = random.randint(1, 20)  # Генеруємо випадкове число
attempt = 0  # Змінна для запису кількості спроб

while attempt != 3:  # Цикл, який триває, поки кількість спроб не дорівнює трьом
    try:
        user_number = int(input("Enter a number (1-50): "))  # Отримуємо число від користувача
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue  # Якщо введене значення не є числом, повторюємо введення

    attempt += 1  # Записуємо спробу

    if 1 <= user_number <= 20:  # Перевіряємо, чи входить число в потрібний діапазон
        if user_number < the_number:
            print("Your number is too low.")  # Якщо число менше за випадкове
            print(f"Remaining attempts: {3 - attempt}")  # Нагадування про кількість спроб
        elif user_number > the_number:
            print("Your number is too high.")  # Якщо число більше за випадкове
            print(f"Remaining attempts: {3 - attempt}")
        else:
            print("Congratulations! You guessed the number.")  # Якщо користувач вгадав число
            print("Great game!")
            break
    else:
        print("Your number is not valid. Try again.")  # Повідомлення про неправильне число

# Повідомлення про програш, якщо число не вгадано за 3 спроби
if attempt == 3 and user_number != the_number:
    print(f"You lost. Guessed number: {the_number}")
