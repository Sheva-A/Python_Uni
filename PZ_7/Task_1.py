initial_amount = float(input("Введіть початкову суму вкладу (грн): "))
interest_rate = float(input("Введіть річну процентну ставку (%): "))
desired_amount = float(input("Введіть бажану кінцеву суму (грн): "))

year = 0
current_amount = initial_amount

while current_amount < desired_amount:
    year += 1
    current_amount += current_amount * (interest_rate / 100)
    print(f"Після {year} року(ів): {current_amount:.2f} грн")

print(f"\nЩоб досягти бажаної суми, знадобиться {year} рік(років).")