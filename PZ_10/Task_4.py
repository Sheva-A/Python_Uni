s = input("Введіть рядок: ")


def is_palindrome_recursive(s):
    """
        Перевіряє рекурсивно, чи є рядок паліндромом (ігнорує регістр і знаки пунктуації).
    """
    s = ''.join(c.lower() for c in s if c.isalnum())
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome_recursive(s[1:-1])

if is_palindrome_recursive(s):
    print("Рядок є паліндромом.")
else:
    print("Рядок не є паліндромом.")