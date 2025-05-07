import random  # Імпортуємо модуль random

secret_pin = str(random.randint(1000, 9999))  # Генеруємо PIN-код
attempts = 0  # Лічильник спроб

print("I have generated a random four-digit PIN. Try to guess it!")

while attempts != 5:  # Дозволяємо до 5 спроб
    user_guess = input("Enter your four-digit PIN: ")

    if len(user_guess) != 4 or not user_guess.isdigit():  # Перевірка формату
        print("Invalid format! Please enter exactly 4 digits.")
        continue

    attempts += 1

    if user_guess == secret_pin:  # Якщо вгадано правильно
        print(f"Congratulations! You guessed the PIN correctly in {attempts} attempts!")
        break

    correct_count = 0
    for i in range(4):
        if secret_pin[i] == user_guess[i]:
            correct_count += 1

    print(f"Incorrect. Correct digits in the correct positions: {correct_count}.")

print(f"Attempts are over. The secret PIN was: {secret_pin}.")
