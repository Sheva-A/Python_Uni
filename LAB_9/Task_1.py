def calculate_cosmic_distance(speed_fraction, time_years):
    if not (0 < speed_fraction < 1):
        raise ValueError("Частка швидкості світла повинна знаходитися в межах від 0 до 1.")
    return speed_fraction * time_years

def calculate_simplified_gravity(mass1, mass2, cosmic_factor=1.0):
    return mass1 * mass2 * cosmic_factor

def calculate_time_dilation(speed_fraction, time_seconds):
    if not (0 < speed_fraction < 1):
        raise ValueError("Частка швидкості світла повинна знаходитися в межах від 0 до 1.")
    return time_seconds / (1 - speed_fraction)

def main():
    print("Вітаємо у Всесвітньому калькуляторі!")

    while True:
        print("\nМеню:")
        print("1 - Обчислити космічну відстань")
        print("2 - Обчислити спрощену гравітацію")
        print("3 - Обчислити сповільнення часу")
        print("0 - Вийти")

        choice = input("Ваш вибір: ").strip()

        if choice == "1":
            print("\nКосмічна відстань")
            try:
                speed = float(input("Введіть частку швидкості світла (від 0 до 1): "))
                time = float(input("Введіть час у роках: "))
                result = calculate_cosmic_distance(speed, time)
                print(f"Відстань: {result:.3f} світлових років.")
            except ValueError as e:
                print(f"Помилка: {e}")

        elif choice == "2":
            print("\nСпрощена гравітація")
            try:
                m1 = float(input("Введіть масу першого об'єкта: "))
                m2 = float(input("Введіть масу другого об'єкта: "))
                factor_input = input("Введіть космічний фактор (або натисніть Enter для 1.0): ").strip()
                factor = float(factor_input) if factor_input else 1.0
                result = calculate_simplified_gravity(m1, m2, factor)
                print(f"Гравітаційна взаємодія: {result:.3f}")
            except ValueError:
                print("Помилка: потрібно ввести числові значення.")

        elif choice == "3":
            print("\nСповільнення часу")
            try:
                speed = float(input("Введіть частку швидкості світла (від 0 до 1): "))
                time = float(input("Введіть час у секундах: "))
                result = calculate_time_dilation(speed, time)
                print(f"Наближене сповільнення часу: {result:.3f} секунд.")
            except ValueError as e:
                print(f"Помилка: {e}")

        elif choice == "0":
            print("До побачення!")
            break

        else:
            print("Невірний вибір. Введіть 1, 2, 3 або 0.")

if __name__ == "__main__":
    main()

