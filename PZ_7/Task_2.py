import random

secret_number = random.randint(1, 100)
attempt = 0

print("Я загадав число від 1 до 100.")
print(f"У тебе є 7 спроб, щоб вгадати його.")

for attempt in range(1,8):
    try:
        guess = int(input(f"Спроба {attempt}: Введи число: "))
    except ValueError:
        print("Будь ласка, введи ціле число.")
        continue

    if guess == secret_number:
        print(f"Вітаю! Ти вгадав число за {attempt} спроб(у/и).")
        break
    elif guess < secret_number:
        print("Загадане число більше.")
    else:
        print("Загадане число менше.")
else:
    print(f"На жаль, ти не вгадав. Загадане число було {secret_number}.")