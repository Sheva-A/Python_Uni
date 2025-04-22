def count_words_in_file(filename="Quote.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        return "Файл не знайдено"

if __name__ == "__main__":
    filename = "quote.txt"
    num_of_words = count_words_in_file(filename)
    print("Кількість слів у файлі:", num_of_words)