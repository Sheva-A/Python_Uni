#Приймаємо числа типу string
input_a = input("Введіть перше число: ")
input_b = input("Введіть друге число: ")

#Перетворюємо числа в тип float
a = float(input_a)
b = float(input_b)

#Виконуємо дії
add_result = a + b
sub_result = a - b
mult_result = a * b
div_result = a / b

#Виводимо результат, перетворюємо в тип string
print("Сума:", str(add_result))
print("Різниця:", str(sub_result))
print("Добуток:", str(mult_result))
print("Частка:", str(div_result))