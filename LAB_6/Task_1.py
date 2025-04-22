import random

def main():
    coins = random.randint(1, 1000)
    print(f"Ви знайшли {coins} золотих монет!")

    try:
        team_size = int(input("Введіть кількість людей у команді: "))
        coins_per_person = coins // team_size
        print(f"Кожен член команди отримує {coins_per_person} монет.")
    except ValueError:
        print("Помилка: введено некоректне значення. Будь ласка, введіть ціле число.")
    except ZeroDivisionError:
        print("Помилка: на команду з 0 людей поділити неможливо!")
    finally:
        print("Пригоди тривають!")

if __name__ == "__main__":
    main()