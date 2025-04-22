import random  #Імпортуємо модуль random

#Функція, яка генерує випадкове число
def set_the_number():
    return random.randint(1, 10)

#Головна функція
def main():

    the_number = set_the_number()  #Генеруємо випадкове число

    while True:  #Нескінченний цикл, який триває, поки користувач не вгадає число
        try:
            user_number = int(input("Enter a number (1-10): "))  #Отримуємо число від користувача
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue  #Якщо введене значення не є числом, повторюємо введення

        if 1 <= user_number <= 10:  #Перевіряємо, чи входить число в потрібний діапазон
            if user_number < the_number:
                print("Your number is too low.")  #Виводимо, якщо число менше за випадкове
            elif user_number > the_number:
                print("Your number is too high.")  #Виводимо, якщо число більше за випадкове
            else:
                print("Congratulations! You guessed the number.")  #Виводимо, якщо користувач вгадав число
                print("Great game!")
                break  #Завершуємо цикл гри
        else:
            print("Your number is not valid. Try again.")  #Повідомлення про число, яке не входить в діапазон


if __name__ == "__main__":
    main()  #Запускаємо програму