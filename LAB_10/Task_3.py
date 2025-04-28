s = input("Введіть числа через пробіл: ").split()

try:
    numbers = [float(x) for x in s]
except ValueError:
    print("Помилка. Вводьте лише числа.")
else:
    def sum_list_recursive(lst):
        """
            Обчислює суму елементів списку рекурсивно.
        """
        if not lst:
            return 0
        return lst[0] + sum_list_recursive(lst[1:])

    print("Сума елементів списку:", sum_list_recursive(numbers))