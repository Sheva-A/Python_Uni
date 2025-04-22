import random  #Імпортуємо модуль random

#Повертає випадковий колір зі списку доступних кольорів
def get_random_color():

    colors = ["red", "orange", "yellow", "green", "blue", "purple"]  #Список доступних кольорів
    return random.choice(colors)  #Вибір кольору зі списку

#Функція визначає, до якої групи належить колір
def get_color_hint(color):
    warm_colors = ["red", "orange", "yellow"]  #Теплі кольори
    cold_colors = ["blue", "green", "purple"]  #Холодні кольори

    if color in warm_colors:
        return "warm"
    elif color in cold_colors:
        return "cold"

#Основна функція
def main():

    secret_color = get_random_color()  #Генеруємо випадковий колір
    attempts = 0 #Змінна для запису кількості спроб

    print("I have chosen a random color. Try to guess it!")  #Вітальне повідомлення
    print("The colors are: red, orange, yellow, green, blue, purple.")  #Доступні кольори

    while attempts != 3:  #Цикл, який триває, поки користувач число спроб не дорівнює трьом
        user_guess = input("Enter your guess: ").lower()  #Отримуємо введення користувача та переводимо у нижній регістр

        #Перевіряємо, чи введений колір є у списку доступних
        if user_guess not in ["red", "orange", "yellow", "green", "blue", "purple"]:
            print("Invalid color! Please choose from red, blue, green, yellow, or purple.")
            continue  #Якщо введене значення не дійсне, повторюємо введення

        attempts += 1  #Записуємо спробу

        if user_guess == secret_color:  #Якщо користувач вгадав колір
            print(f"Congratulations! You guessed the color correctly in {attempts} attempts!")
            break  #Виходимо з циклу

        #Отримуємо підказку про групу кольору
        hint = get_color_hint(secret_color)
        print(f"Incorrect guess. The secret color belongs to the '{hint}' category.")

    #Повідомлення про кінець гри, якщо користувач не вгадав колір за 3 спроби
    print(f"Out of attempts! The secret color was: {secret_color}.")

if __name__ == "__main__":
    main()  #Запускаємо програму