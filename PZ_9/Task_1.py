def process_data(data, operation, dict_mode='values'):
    """
    Застосовує функцію до кожного елемента колекції.
    Працює зі списками, кортежами та словниками.
    Повертає нову колекцію з результатами.
    """
    try:
        if not callable(operation):
            raise TypeError("operation має бути функцією")

        if isinstance(data, list):
            return [operation(x) for x in data]
        elif isinstance(data, tuple):
            return tuple(operation(x) for x in data)
        elif isinstance(data, dict):
            if dict_mode == 'keys':
                return {operation(k): v for k, v in data.items()}
            elif dict_mode == 'values':
                return {k: operation(v) for k, v in data.items()}
            elif dict_mode == 'items':
                return {operation(k): operation(v) for k, v in data.items()}
            else:
                return "Помилка: невідомий режим dict_mode"
        else:
            return "Помилка: тип колекції не підтримується"
    except Exception as e:
        return f"Помилка: {e}"


def filter_data(data, predicate):
    """
    Повертає елементи, які відповідають умові.
    Приймає список, кортеж або словник і функцію-предикат.
    Повертає нову колекцію того ж типу.
    """
    try:
        if not callable(predicate):
            raise TypeError("predicate має бути функцією")

        if isinstance(data, list):
            return [x for x in data if predicate(x)]
        elif isinstance(data, tuple):
            return tuple(x for x in data if predicate(x))
        elif isinstance(data, dict):
            return {k: v for k, v in data.items() if predicate((k, v))}
        else:
            return "Помилка: тип колекції не підтримується"
    except Exception as e:
        return f"Помилка: {e}"


def combine_values(*args, separator='', initial=None):
    """
    Об'єднує числа або рядки залежно від типу першого аргументу.
    Для чисел додає, для рядків з'єднує з роздільником.
    Може використовувати початкове значення або роздільник.
    """
    try:
        if not args:
            return initial if initial is not None else 0

        first = args[0]

        if isinstance(first, str):
            return separator.join(str(x) for x in args)
        elif isinstance(first, (int, float)):
            result = initial if initial is not None else 0
            for x in args:
                if not isinstance(x, (int, float)):
                    raise TypeError("усі аргументи мають бути числами")
                result += x
            return result
        else:
            return "Помилка: підтримуються тільки рядки або числа"
    except Exception as e:
        return f"Помилка: {e}"


# Тестування

print("Process_data")
print(process_data([1, 2, 3], lambda x: x * 2))
print(process_data((4, 5, 6), lambda x: x + 1))
print(process_data({'a': 1, 'b': 2}, lambda x: x * 10))
print(process_data({'a': 1, 'b': 2}, lambda x: x.upper(), dict_mode='keys'))
print(process_data({'x': 1, 'y': 2}, lambda x: str(x), dict_mode='items'))

print("\nFilter_data")
print(filter_data([1, 2, 3, 4], lambda x: x % 2 == 0))
print(filter_data((5, 6, 7), lambda x: x > 5))
print(filter_data({'a': 1, 'b': 2, 'c': 3}, lambda item: item[1] > 1))

print("\nCombine_values")
print(combine_values(1, 2, 3))
print(combine_values(1, 2, 3, initial=10))
print(combine_values("Hello", "world", separator=" "))
print(combine_values("a", "b", "c", separator="-"))
print(combine_values(1, "2", 3))

