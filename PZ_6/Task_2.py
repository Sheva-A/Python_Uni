stock = 20
order = int(input("Введіть кількість товару: "))

if order <= 0:
    print("Помилка: некоректна кількість!")
    exit()
elif order > stock:
    print("На складі недостатньо товару!")
    exit()

print("Ваше замовлення прийнято!")