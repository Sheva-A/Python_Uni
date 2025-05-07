import random  # Імпортуємо модуль для роботи з випадковістю

# Функція для "очищення" екрана (імітація через багато перенесень рядка)
def clear_screen():
    print("\n" * 100)

# Списки слів у різних категоріях
animals = ["лев", "ворон", "акула", "мураха", "дельфін"]
plants = ["дуб", "мухомор", "кактус", "орхідея", "соняшник"]
people = ["курбас", "кідрук", "ділан", "шекспір", "шевченко"]
imaginary = ["дракон", "єдиноріг", "гоблін", "фенікс", "русалка"]
technology = ["камінь", "стілець", "авто", "телефон", "комп'ютер"]

# Об'єднання всіх слів в один список для перевірки введення
all_words = animals + plants + people + imaginary + technology

# Лічильник спроб та список введених слів
attempts = 0
guessed_words = []

# Випадкові числа, які визначають, на яких спробах буде надано підказки
h1 = random.choice([1, 5])
h2 = random.choice([6, 10])
h3 = random.choice([11, 15])
ah1 = random.choice([1, 5])
ah2 = random.choice([6, 10])

# Виведення вступної інформації та можливих варіантів
print("Вгадай об'єкт!")
print("\nМожливі категорії:")
print("1 — Тварини")
print("2 — Рослини")
print("3 — Відомі люди")
print("4 — Вигадані істоти")
print("5 — Техніка")

# Виводимо слова для кожної категорії
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

# Старт гри
print("\nПочнемо гру!")
print("Якщо знатимеш відповідь до закінчення спроб, обери finish (f).")

# Вибір категорії користувачем, але відбувається змішування з іншим набором
user_category = int(input("\nОбери категорію (1-5) (вони перемішані): "))

# Визначаємо справжню категорію та слово на основі вибору користувача
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

# Основний цикл гри — поки не вичерпано спроби
while attempts != h3 + 1:
    try:
        # Отримуємо відповідь користувача
        guess = input("Введіть слово: ").strip().lower()
        guessed_words.append(guess)

        # Якщо гравець хоче завершити гру раніше
        if guess == "finish" or guess == "f":
            break
        elif (guess not in all_words) and (guess == "finish" or guess == "f"):
            print("Цього слова немає в списку можливих.")
            continue

        # Збільшуємо кількість спроб
        attempts = attempts + 1

        # Підказки на певних етапах
        if attempts == h1:
            print(f"Підказка: Об'єкт є — {category}.")
        elif attempts == h2:
            print(f"Підказка: Перша літера об'єкта — '{secret_word[0].upper()}'.")
        elif attempts == h3:
            print(f"Підказка: Остання літера об'єкта — '{secret_word[-1].upper()}'.")

        # Додаткові (іноді заплутуючі) підказки
        if attempts == ah1:
            print(f"Підказка: Довжина слова — '{len(secret_word) + random.choice([-3, 3])}'.")
        elif attempts == ah2:
            print(f"Підказка: Перша літера слова — '{secret_word[random.choice([2, -1])].upper()}'.")
    except:
        print("Щось пішло не так. Спробуйте знову.")
    finally:
        print(f"Спроба {attempts}.")

# Імітуємо очищення екрана після завершення гри
clear_screen()

# Перевіряємо першу спробу
first_try = guessed_words[0]

print(f"Спроби закінчилися.")
input_first_guess = input("Яке слово ви вводили першим, коли намагались вгадати?: ")

# Перевірка уважності та успішності
if input_first_guess == first_try:
    if secret_word in guessed_words:
        print(f"Ви були уважними та вгадали слово! Загадане слово було: {secret_word}")
    else:
        print(f"Ви були уважними, проте НЕ вгадали слово! Загадане слово було: {secret_word}")
else:
    print("Ви не уважні!")
