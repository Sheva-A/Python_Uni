n = input("Введіть невід'ємне ціле число: ")

if not n.isdigit():
    print("Помилка. Введіть невід'ємне ціле число.")
else:
    n = int(n)

    def fibonacci_recursive(n):
        """
            Повертає n-те число Фібоначчі, використовуючи рекурсію.
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

    print(f"{n}-те число Фібоначчі:", fibonacci_recursive(n))
