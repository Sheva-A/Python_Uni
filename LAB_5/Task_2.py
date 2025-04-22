import random #Імпортуємо модуль random

#Функція, яка генерує випадкове число
def set_the_number():
    return random.randint(1, 50)

#Головна функція
def main():

    the_number = set_the_number() #Генеруємо випадкове число

    while True: #Нескінченний цикл, який триває, поки користувач не вгадає число

        try:
            user_number = int(input("Enter a number (1-50): "))  #Отримуємо число від користувача
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue  #Якщо введене значення не є числом, повторюємо введення

        if 1 <= user_number <= 50: #Перевіряємо, чи входить число в потрібний діапазон
            if abs(the_number - user_number) > 10:
                print("Far.") #Виводимо, якщо число більше ніж за десять позицій від загаданого
            elif 3 < abs(the_number - user_number) <= 10:
                print("Close.") #Виводимо, якщо число більше ніж за 3 позиції від загаданого
            elif 1 < abs(the_number - user_number) <= 3:
                print("Very close!") #Виводимо, якщо число менше ніж за 3 позиції від загаданого
            else:
                print("Congratulations! You guessed the number.") #Виводимо, якщо користувач вгадав число
                print("Great game!")
                break #Завершуємо цикл гри
        else:
            print("Your number is not valid. Try again.") #Повідомлення про число, яке не входить в діапазон


if __name__ == "__main__":
    main() #Запускаємо програму