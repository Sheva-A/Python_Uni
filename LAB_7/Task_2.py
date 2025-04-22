import random

living = ["лев", "дуб", "ворон", "акула", "людина", "мухомор", "кактус", "мураха", "дельфін", "орхідея"]
non_living = ["камінь", "стілець", "авто", "телефон", "олівець", "книга", "комп'ютер", "лампа", "дзеркало", "тарілка"]

all_words = living + non_living

secret_word = random.choice(all_words)

if secret_word in living:
    category = "Живе"
else:
    category = "Неживе"

print("Вгадай об'єкт! У тебе є 10 спроб.")
print("Можливі категорії: Живе, Неживе.")
print("Слова категорії 'Живе':")
print(", ".join(living))
print("Слова категорії 'Неживе':")
print(", ".join(non_living))
print("Почнемо гру!")

attempts = 0

while attempts < 10:
    try:
        guess = input("Введіть слово: ").strip().lower()


        if guess not in all_words:
            print("Цього слова немає в списку можливих.")
            continue

        if guess == secret_word:
            if random.choice([True, False]):
                print(f"Молодець! Ти переміг. Загаданий об'єкт: {secret_word}")
            else:
                print(f"Упс.. Комп'ютер програв. Загаданий об'єкт: {secret_word}")
            break
        else:
            print("Ви не вгадали.")

        attempts = attempts + 1

        if attempts == 3:
            print(f"Підказка 1: Об'єкт є — {category.lower()}.")
        elif attempts == 6:
            print(f"Підказка 2: Перша літера об'єкта — '{secret_word[0].upper()}'.")
        elif attempts == 9:
            print(f"Підказка 3: Остання літера об'єкта — '{secret_word[-1].upper()}'.")

    except:
        print("Щось пішло не так. Спробуйте знову.")

    finally:
        print("Залишилось спроб:", 10 - attempts)

print(f"Ви не вгадали. Загаданий об'єкт був: {secret_word}")