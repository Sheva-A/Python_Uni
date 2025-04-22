num_products = int(input("Скільки товарів ви хочете ввести? "))
products = []

for i in range(num_products):
    print(f"\nТовар {i + 1}:")
    name = input("Назва товару: ")
    price = float(input("Ціна: "))
    quantity = int(input("Кількість: "))
    products.append((name, price, quantity))

print("\n{:<20}{:>10}{:^8}".format("Назва товару", "Ціна", "К-сть"))
print("-" * 38)

for name, price, quantity in products:
    print("{:<20}{:>10.2f}{:^8}".format(name, price, quantity))