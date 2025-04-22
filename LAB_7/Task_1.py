import random

living = ["лев", "дуб", "ворон", "акула", "людина", "мухомор", "кактус", "мураха", "дельфін", "орхідея"]
non_living = ["камінь", "стілець", "машина", "телефон", "олівець", "книга", "комп'ютер", "лампа", "дзеркало", "тарілка"]
imaginary = ["дракон", "єдиноріг", "гоблін", "фенікс", "пегас", "русалка", "троль", "джин", "мавка", "водяний"]

all_words = living + non_living + imaginary

secret_word = random.choice(all_words)

if secret_word in living:
    category = "Живе"
elif secret_word in non_living:
    category = "Неживе"
else:
    category = "Вигадане"

print("Вгадай об'єкт! У тебе є 10 спроб.")
print("Можливі категорії: Живе, Неживе, Вигадане.")
print("Слова категорії 'Живе':")
print(", ".join(living))
print("Слова категорії 'Неживе':")
print(", ".join(non_living))
print("Слова категорії 'Вигадане':")
print(", ".join(imaginary))
print("Почнемо гру!")

attempts = 0

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

        if attempts == 5:
            print("Підказка: слово належить до категорії -", category)

        attempts = attempts + 1

    except:
        print("Щось пішло не так. Спробуйте знову.")

    finally:
        print("Залишилося спроб:", 10 - attempts)


print(f"Ви не вгадали. Загадане слово було: {secret_word}")