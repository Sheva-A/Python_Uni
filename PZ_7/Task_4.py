while True:
    try:
        n = int(input("Введіть ціле число, не менше за 0: "))
        if n < 0:
            print("Число повинно бути більшим за 0.")
            continue
        break
    except ValueError:
        print("Це не ціле число. Спробуйте ще раз.")

fact = 1
i = 1
steps = ""

while i <= n:
    fact *= i
    steps += f"{i}*" if i < n else f"{i}"
    i += 1

print(f"{n}! = {steps} = {fact}")