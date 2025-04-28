import random


def generate_secret_code():
    digits = list('0123456789')
    random.shuffle(digits)
    return ''.join(digits[:4])


def get_bulls_and_cows(secret_code, guess):
    bulls = sum(sc == gc for sc, gc in zip(secret_code, guess))
    cows = sum(min(secret_code.count(digit), guess.count(digit)) for digit in set(guess)) - bulls
    return bulls, cows


def is_valid_guess(guess):
    return guess.isdigit() and len(guess) == 4 and len(set(guess)) == 4


def play_game():
    print("Вітаю у грі 'Таємний код'!")
    secret_code = generate_secret_code()
    attempts = 0

    while True:
        guess = input("Введіть вашу спробу (4 різні цифри): ")

        if not is_valid_guess(guess):
            print("Некоректне введення. Введіть 4 різні цифри.")
            continue

        attempts += 1
        bulls, cows = get_bulls_and_cows(secret_code, guess)

        if bulls == 4:
            print(f"Вітаємо! Ви вгадали код {secret_code} за {attempts} спроб(у/и)!")
            break
        else:
            print(f"{bulls} бик(и), {cows} корова(и). Спробуйте ще!")


if __name__ == "__main__":
    play_game()
