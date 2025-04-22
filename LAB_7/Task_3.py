import random

def clear_screen():
    print("\n" * 100)

animals = ["лев", "ворон", "акула", "мураха", "дельфін"]
plants = ["дуб", "мухомор", "кактус", "орхідея", "соняшник"]
people = ["курбас", "кідрук", "ділан", "шекспір", "шевченко"]
imaginary = ["дракон", "єдиноріг", "гоблін", "фенікс", "русалка"]
technology = ["камінь", "стілець", "авто", "телефон", "комп'ютер"]

all_words = animals + plants + people + imaginary + technology

attempts = 0
guessed_words = []

h1 = random.choice([1, 5])
h2 = random.choice([6, 10])
h3 = random.choice([11, 15])
ah1 = random.choice([1, 5])
ah2 = random.choice([6, 10])

print("Вгадай об'єкт!")
print("\nМожливі категорії:")
print("1 — Тварини")
print("2 — Рослини")
print("3 — Відомі люди")
print("4 — Вигадані істоти")
print("5 — Техніка")

print("\nСлова категорії 'Тварини':")
print(", ".join(animals))
print("\nСлова категорії 'Рослини':")
print(", ".join(plants))
print("\nСлова категорії 'Відомі люди':")
print(", ".join(people))
print("\nСлова категорії 'Вигадані істоти':")
print(", ".join(imaginary))
print("\nСлова категорії 'Техніка':")
print(", ".join(technology))

print("\nПочнемо гру!")
print("Якщо знатимеш відповідь до закінчення спроб, обери finish (f).")

user_category = int(input("\nОбери категорію (1-5) (вони перемішані): "))

if user_category == 1:
    category = "Рослини"
    secret_word = random.choice(plants)
elif user_category == 2:
    category = "Відомі люди"
    secret_word = random.choice(people)
elif user_category == 3:
    category = "Тварини"
    secret_word = random.choice(animals)
elif user_category == 4:
    category = "Техніка"
    secret_word = random.choice(technology)
else:
    category = "Вигадані істоти"
    secret_word = random.choice(imaginary)

while attempts != h3 + 1:
    try:
        guess = input("Введіть слово: ").strip().lower()
        guessed_words.append(guess)

        if guess == "finish" or guess == "f":
            break
        elif (guess not in all_words) and (guess == "finish" or guess == "f"):
            print("Цього слова немає в списку можливих.")
            continue

        attempts = attempts + 1

        if attempts == h1:
            print(f"Підказка: Об'єкт є — {category}.")
        elif attempts == h2:
            print(f"Підказка: Перша літера об'єкта — '{secret_word[0].upper()}'.")
        elif attempts == h3:
            print(f"Підказка: Остання літера об'єкта — '{secret_word[-1].upper()}'.")

        if attempts == ah1:
            print(f"Підказка: Довжина слова — '{len(secret_word) + random.choice([-3, 3])}'.")
        elif attempts == ah2:
            print(f"Підказка: Перша літера слова — '{secret_word[random.choice([2, -1])].upper()}'.")

    except:
        print("Щось пішло не так. Спробуйте знову.")

    finally:
        print(f"Спроба {attempts}.")

clear_screen()

first_try = guessed_words[0]

print(f"Спроби закінчилися.")
input_first_guess = input("Яке слово ви вводили першим, коли намагались вгадати?: ")

if input_first_guess == first_try:
    if secret_word in guessed_words:
        print(f"Ви були уважними та вгадали слово! Загадане слово було: {secret_word}")
    else:
        print(f"Ви були уважними, проте НЕ вгадали слово! Загадане слово було: {secret_word}")
else:
    print("Ви не уважні!")