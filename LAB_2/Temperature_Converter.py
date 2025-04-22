#Функція перевіряє, чи може бути введений текст числом.
#Повертає True, якщо так, інакше повертає False.
def is_float(temp_celsius):
    try:
        float(temp_celsius)
        return True
    except ValueError:
        return False

#Функція перетворює Цельсія у Фарангейт
def convert(temp_celsius):
    return round(temp_celsius * 9 / 5 + 32, 2)

def main():
    #Цикл, який працює поки не буде введено число
    while True:

        temp_celsius = input("Enter temperature in Celsius: ") #Отримуємо значення від користувача

        # Якщо введене значення є числом, відбувається конвертація, вивід відповідного повідомлення та зупинка циклу.
        # Якщо введено некоректне значення, відбувається вивід про помилку
        if is_float(temp_celsius): #Перевіряємо чи може текст бути числом
            temp_celsius = float(temp_celsius) #Конвертуємо текст у число
            temp_fahrenheit = convert(temp_celsius) #Перетворюємо Цельсія у Фарангейт
            print(f"{temp_celsius} degrees Celsius equals {temp_fahrenheit} degrees Fahrenheit.") #Вивід повідомлення
            break #Зупинка циклу
        else:
            # Якщо введено не число, виводимо відповідне повідомлення
            print("Invalid input.")

#Запускаємо програму
if __name__ == "__main__":
    main()