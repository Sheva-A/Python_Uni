#Додаємо модуль tkinter
import tkinter as tk

#Функція перевіряє, чи може бути введений текст числом.
#Повертає True, якщо так, інакше повертає False.
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

#Функція зчитує та перевіряє введене користувачем значення.
#Якщо введене значення є числом, відбувається конвертація та вивід відповідного повідомлення.
#Якщо введено некоректне значення, відбувається вивід про помилку.
def convert():
    temp_celsius = entry.get() #Отримуємо текст

    if is_float(temp_celsius): #Перевіряємо чи може текст бути числом
        temp_celsius = float(temp_celsius) #Конвертуємо текст у число
        temp_fahrenheit = round(temp_celsius * 9 / 5 + 32, 2) #Перетворюємо Цельсія у Фарангейт
        # Оновлюємо результат
        result_label.config(text=f"{temp_celsius} °C = {temp_fahrenheit} °F", fg="white", bg="#191970")
    else:
        #Якщо введено не число, оновлюємо результат
        result_label.config(text="Invalid input. Enter a number.", fg="#f08080", bg="#191970")


window = tk.Tk() #Створюємо вікно
window.title("Celsius to Fahrenheit Converter") #Заголовок вікна
window.geometry("400x300+50+100") #Розміри вікна та відступи праворуч та згори
window.config(bg="#191970") #Колір тла

entry_label = tk.Label(window, text="Enter temperature in Celsius:", font=("Arial", 12)) #Створюємо текст
entry_label.pack(pady=10) #Розміщуємо текст у вікні
entry = tk.Entry(window, font=("Arial", 14)) #Створюємо поле для введення
entry.pack(pady=10) #Розміщуємо поле у вікні

#Створюємо кнопку для конвертації
convert_button = tk.Button(window, text="Convert", font=("Arial", 12), command=convert)
convert_button.pack(pady=10) #Розміщуємо кнопку у вікні

#Створюємо текст для результату
result_label = tk.Label(window, text="", font=("Arial", 14, "bold"), bg="#191970")
result_label.pack(pady=10) #Розміщуємо текст у вікні

window.mainloop() #Запускаємо головний цикл подій