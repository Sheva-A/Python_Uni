import random #Імпортуємо модуль random

#Функція, яка генерує випадкове число
def set_the_number():
    return random.randint(1, 20)

#Головна функція
def main():

    the_number = set_the_number() #Генеруємо випадкове число
    attempt = 0 #Змінна для запису кількості спроб

    while attempt != 3: #Цикл, який триває, поки користувач число спроб не дорівнює трьом

        try:
            user_number = int(input("Enter a number (1-50): "))  #Отримуємо число від користувача
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue  #Якщо введене значення не є числом, повторюємо введення

        attempt += 1 #Записуємо спробу

        if 1 <= user_number <= 20: #Перевіряємо, чи входить число в потрібний діапазон
            if user_number < the_number:
                print("Your number is too low.") #Виводимо, якщо число менше за випадкове
                print(f"Remaining attempts: {3 - attempt}") #Нагадування про кількість спроб
            elif user_number > the_number:
                print("Your number is too high.") #Виводимо, якщо число більше за випадкове
                print(f"Remaining attempts: {3 - attempt}") #Нагадування про кількість спроб
            else:
                print("Congratulations! You guessed the number.") #Виводимо, якщо користувач вгадав число
                print("Great game!")
                break #Завершуємо цикл гри
        else:
            print("Your number is not valid. Try again.") #Повідомлення про число, яке не входить в діапазон

    #Повідомлення про програш гри, якщо користувач не вгадав число за 3 спроби
    print(f"You lost. Guessed number: {the_number}")


if __name__ == "__main__":
    main() #Запускаємо програму