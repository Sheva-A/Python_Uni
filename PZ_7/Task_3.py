lower = int(input("Введіть нижню межу діапазону: "))
upper = int(input("Введіть верхню межу діапазону: "))

prime_numbers = []

for num in range(lower, upper + 1):
    if num > 1:
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)

if prime_numbers:
    print("Прості числа в діапазоні від", lower, "до", upper, ":")
    print(prime_numbers)
else:
    print("У вказаному діапазоні немає простих чисел.")