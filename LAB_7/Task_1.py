import random  # Імпортуємо модуль для випадкового вибору

# Списки слів за категоріями
living = ["лев", "дуб", "ворон", "акула", "людина", "мухомор", "кактус", "мураха", "дельфін", "орхідея"]
non_living = ["камінь", "стілець", "машина", "телефон", "олівець", "книга", "комп'ютер", "лампа", "дзеркало", "тарілка"]
imaginary = ["дракон", "єдиноріг", "гоблін", "фенікс", "пегас", "русалка", "троль", "джин", "мавка", "водяний"]

# Об'єднуємо всі слова в один список
all_words = living + non_living + imaginary

# Випадкове слово для відгадування
secret_word = random.choice(all_words)

# Визначаємо категорію обраного слова
if secret_word in living:
    category = "Живе"
elif secret_word in non_living:
    category = "Неживе"
else:
    category = "Вигадане"

# Інформація для гравця
print("Вгадай об'єкт! У тебе є 10 спроб.")
print("Можливі категорії: Живе, Неживе, Вигадане.")
print("Слова категорії 'Живе':")
print(", ".join(living))
print("Слова категорії 'Неживе':")
print(", ".join(non_living))
print("Слова категорії 'Вигадане':")
print(", ".join(imaginary))
print("Почнемо гру!")

# Починаємо гру
attempts = 0  # Лічильник спроб

while attempts < 10:
    try:
        guess = input("Введіть слово: ").strip().lower()

        if guess not in all_words:
            print("Цього слова немає в списку. Спробуйте знову.")
            continue

        if guess == secret_word:
            print(f"Ви вгадали! Слово було: {secret_word}")
            break
        else:
            print("Ви не вгадали.")

        if attempts == 4:  # Після 5-ї спроби (індексація з 0)
            print("Підказка: слово належить до категорії -", category)

        attempts += 1

    except:
        print("Щось пішло не так. Спробуйте знову.")

    finally:
        print("Залишилося спроб:", 10 - attempts)

# Якщо не вгадали за 10 спроб
if attempts == 10:
    print(f"Ви не вгадали. Загадане слово було: {secret_word}")