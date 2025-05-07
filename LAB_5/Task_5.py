import random  # Імпортуємо модуль random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]  # Список доступних кольорів
secret_color = random.choice(colors)  # Випадковий вибір кольору
attempts = 0  # Лічильник спроб

print("I have chosen a random color. Try to guess it!")
print("The colors are: red, orange, yellow, green, blue, purple.")

while attempts != 3:
    user_guess = input("Enter your guess: ").lower()

    if user_guess not in colors:
        print("Invalid color! Please choose from red, blue, green, yellow, or purple.")
        continue

    attempts += 1

    if user_guess == secret_color:
        print(f"Congratulations! You guessed the color correctly in {attempts} attempts!")
        break

    if secret_color in ["red", "orange", "yellow"]:
        hint = "warm"
    elif secret_color in ["blue", "green", "purple"]:
        hint = "cold"

    print(f"Incorrect guess. The secret color belongs to the '{hint}' category.")

print(f"Out of attempts! The secret color was: {secret_color}.")
