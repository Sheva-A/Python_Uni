#Отримуємо введений рядок
input_str = input("Введіть числа, розділені комами: ")

#Розбиваємо рядок на список
str_list = input_str.split(",")

#Перетворюємо список рядків у список чисел float
num_list = [float(num) for num in str_list]

#Обчислюємо суму та середнє значення
sum_result = sum(num_list)
average_result = sum_result / len(num_list)

#Виводимо результати
print("Список чисел:", num_list)
print("Сума чисел:", sum_result)
print("Середнє значення:", average_result)