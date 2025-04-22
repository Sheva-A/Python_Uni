import random


def main():
    code = random.randint(100, 999)
    attempts = 0

    print("Гра почалась. У вас 5 спроб, щоб зламати код!")

    while attempts != 5:
        try:
            guess = int(input("Введіть трьохзначний код: "))

            if guess < 100 or guess > 999:
                print("Введіть ТРЬОХЗНАЧНЕ число!")
                continue

            if guess == code:
                print("Вітаємо! Ви зламали сейф!")
                return
            elif guess < code:
                print("Код більший.")
            else:
                print("Код менший.")

        except ValueError:
            print("Помилка: введіть лише числа!")

        finally:
            attempts += 1
            if attempts != 5:
                print("Залишилось спроб:", 5-attempts)
            else:
                print(f"Спроби закінчилися! Код сейфу був: {code}")


if __name__ == "__main__":
    main()