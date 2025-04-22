import random  #Імпортуємо модуль random

#Генерує випадковий чотиризначний PIN-код
def generate_pin():
    return str(random.randint(1000, 9999))

#Підраховує кількість правильних цифр у правильних позиціях
def count_correct_digits(secret_pin, user_guess):
    correct_count = 0
    for i in range(len(secret_pin)):  #Проходимо по всіх індексах PIN-коду
        if secret_pin[i] == user_guess[i]:  #Якщо цифри збігаються
            correct_count += 1
    return correct_count #Повертає кількість збігів цифр на правильних позиціях.

#Основна функція
def main():

    secret_pin = generate_pin()  #Генеруємо PIN-код
    attempts = 0  #Змінна для запису кількості спроб

    print("I have generated a random four-digit PIN. Try to guess it!")

    while attempts != 5:  #Цикл, який триває, поки користувач число спроб не дорівнює п'ятьом
        user_guess = input("Enter your four-digit PIN: ")  #Отримуємо число від користувача

        #Перевіряємо, чи введені дані відповідають формату
        if len(user_guess) != 4 or not user_guess.isdigit():
            print("Invalid format! Please enter exactly 4 digits.")
            continue  #Знову запитуємо введення, якщо дані не відповідають формату

        attempts += 1  #Записуємо спробу

        if user_guess == secret_pin:  #Якщо PIN-код введений правильно
            print(f"Congratulations! You guessed the PIN correctly in {attempts} attempts!")
            break  #Виходимо з циклу

        #Обчислюємо кількість правильних цифр на правильних позиціях
        correct_digits = count_correct_digits(secret_pin, user_guess)
        print(f"Incorrect. Correct digits in the correct positions: {correct_digits}.")

    #Повідомлення про кінець гри, якщо користувач не вгадав число за 5 спроб
    print(f"Attempts are over. The secret PIN was: {secret_pin}.")


if __name__ == "__main__":
    main()  #Запускаємо програму