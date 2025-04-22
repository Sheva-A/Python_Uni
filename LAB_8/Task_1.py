text = input("Введіть рядок: ")

vowels_ukr = "аеєиіїоуюяАЕЄИІЇОУЮЯ"
consonants_ukr = "бвгґджзйклмнпрстфхцчшщБВГҐДЖЗЙКЛМНПРСТФХЦЧШЩ"

vowel_count = 0
consonant_count = 0
found_vowels = []

for char in text:
    if char in vowels_ukr:
        vowel_count += 1
        found_vowels.append(char)
    elif char in consonants_ukr:
        consonant_count += 1

print("Кількість голосних літер:", vowel_count)
print("Кількість приголосних літер:", consonant_count)
print("Список голосних літер:", found_vowels)