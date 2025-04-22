def main():
    try:
        score = int(input("Введіть кількість набраних очок (від 0 до 100): "))

        if score < 0 or score > 100:
            raise ValueError("Некоректне введення! Кількість очок повинна бути в межах від 0 до 100.")

        if 0 <= score <= 49:
            rating = "Початківець"
            multiplier = 1
        elif 50 <= score <= 69:
            rating = "Срібний гравець"
            multiplier = 1.5
        elif 70 <= score <= 89:
            rating = "Золотий гравець"
            multiplier = 2
        elif 90 <= score <= 100:
            rating = "Платиновий гравець"
            multiplier = 3

        final_score = score * multiplier
        print(f"Ваш рейтинг: {rating}! Ви отримали {final_score} балів (множник ×{multiplier})!")

    except ValueError:
        print("Помилка: введено некоректне значення. Кількість очок повинна бути цілим числом у межах від 0 до 100.")
    finally:
        print("Дякуємо за гру!")


if __name__ == "__main__":
    main()