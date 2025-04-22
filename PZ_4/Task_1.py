number = int(input("Введіть трицифрове число: "))

if  number//100 == number%10:
    print(f"Число {number} є паліндромом")
else:
    print(f"Число {number} не є паліндромом")