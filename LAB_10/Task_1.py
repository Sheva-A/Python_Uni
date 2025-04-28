n = input("Введіть невід'ємне ціле число: ")

if not n.isdigit():
    print("Помилка. Введіть невід'ємне ціле число.")
else:
    n = int(n)

    def factorial_recursive(n):
        """
            Обчислює факторіал числа n рекурсивним методом.
        """
        if n == 0:
            return 1
        return n * factorial_recursive(n - 1)

    print("Факторіал:", factorial_recursive(n))