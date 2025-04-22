password = input("Введіть пароль: ")

if len(password) < 8:
    print("Пароль надто короткий!")
    exit()
elif password == "password" or password == "12345678":
    print("Пароль занадто простий!")
    exit()

print("Вхід дозволено!")