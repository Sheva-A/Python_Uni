import random

def cross_river():
    try:
        wood = int(input("Скільки деревини ви зібрали для плоту (від 1 до 10)? "))
        if wood < 3:
            print("Деревини замало, пліт затонув!")
            return False
    except ValueError:
        print("Це не число!")
        return False
    return True

def escape_pirates():
    try:
        choice = input("Як ви будете тікати? (бігти/сховатися/битися): ").strip().lower()
        if choice not in ["бігти", "сховатися", "битися"]:
            raise ValueError
    except ValueError:
        print("Такого варіанту немає, пірати вас спіймали!")
        return False
    return True

def open_treasure():
    secret_code = random.randint(10, 99)
    try:
        code = int(input("Введіть двозначний код для відкриття скрині: "))
        if code != secret_code:
            print("Неправильний код, скриня вибухнула! Гру завершено.")
            return False
        print("Скарб ваш, ви врятовані!")
    except ValueError:
        print("Це не число! Гру завершено.")
        return False
    return True

def main():
    try:
        print("Ласкаво просимо до гри 'Втеча з острова піратів'!")
        if not cross_river():
            return
        if not escape_pirates():
            return
        if not open_treasure():
            return
    finally:
        print("Гра завершена. Дякуємо за участь у пригоді!")

if __name__ == "__main__":
    main()