# Інвентаризація товарів
# Створення списку товарів
products = [
    {"name": "Ноутбук", "quantity": 10, "price": 25000, "category": "електроніка"},
    {"name": "Смартфон", "quantity": 5, "price": 15000, "category": "електроніка"},
    {"name": "Футболка", "quantity": 20, "price": 400, "category": "одяг"},
    {"name": "Джинси", "quantity": 7, "price": 800, "category": "одяг"},
    {"name": "Хліб", "quantity": 50, "price": 20, "category": "продукти"},
    {"name": "Молоко", "quantity": 30, "price": 25, "category": "продукти"},
    {"name": "Мікрохвильовка", "quantity": 3, "price": 3000, "category": "електроніка"}
]

# Виведення таблиці з товарами
print("\n{:<15} {:<10} {:<15} {:<15}".format("Назва", "Кількість", "Ціна за одиницю", "Категорія"))
print("-" * 60)
for item in products:
    print("{:<15} {:<10} {:<15} {:<15}".format(item["name"], item["quantity"], item["price"], item["category"]))


# Функція для пошуку та редагування товару
def search_and_edit():
    criterion = input("\nПошук за (name/category): ").strip().lower()
    value = input("Введіть значення для пошуку: ").strip()

    found = False
    for product in products:
        if product.get(criterion) and product[criterion].lower() == value.lower():
            found = True
            print("\nЗнайдено товар:")
            print(product)

            field = input("Що хочете змінити? (quantity/price): ").strip().lower()
            if field in ["quantity", "price"]:
                try:
                    new_value = float(input(f"Нове значення для {field}: "))
                    if new_value < 0:
                        raise ValueError("Значення не може бути меншим за 0.")
                    product[field] = new_value if field == "price" else int(new_value)
                    print("Товар успішно оновлено.")
                except ValueError as e:
                    print("Помилка:", e)
            else:
                print("Невідоме поле для оновлення.")
    if not found:
        print("Товар не знайдено.")


# Функція для аналітики складу
def analytics():
    category_summary = {}
    for product in products:
        category = product["category"]
        total = product["quantity"] * product["price"]
        category_summary[category] = category_summary.get(category, 0) + total

    print("\nЗагальна вартість по категоріях:")
    for category, total in category_summary.items():
        print(f"{category}: {total} грн")

    max_category = max(category_summary, key=category_summary.get)
    print(f"\nКатегорія з найбільшою вартістю: {max_category} ({category_summary[max_category]} грн)")

    threshold = 5
    print(f"\nТовари, кількість яких менше {threshold}:")
    for product in products:
        if product["quantity"] < threshold:
            print(f"- {product['name']} ({product['quantity']} шт.)")


# Виклик функцій
search_and_edit()
analytics()
