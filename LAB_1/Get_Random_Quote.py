import requests
import urllib3
from Count_Words import count_words_in_file

def get_random_quote():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    response = requests.get("https://api.quotable.io/random", verify=False)

    if response.status_code == 200:
        data = response.json()
        quote = f'"{data["content"]}"-{data["author"]}'
        return quote
    else:
        return "Не вдалося отримати цитату"

def save_quote_to_file(quote, filename="Quote.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(quote)

def main():
    quote = get_random_quote()
    print(quote)
    save_quote_to_file(quote)
    num_of_words_in_file = count_words_in_file()
    print("Кількість слів у файлі:", num_of_words_in_file)

if __name__ == "__main__":
    main()