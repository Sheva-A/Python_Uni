text = "Замовнику варто було б навчитися розуміти свої бажання!"

cleaned = ""
for char in text:
    if char.isalnum():
        cleaned += char.lower()

counts = {}
for char in cleaned:
    if char in counts:
        counts[char] += 1
    else:
        counts[char] = 1

print("Кількість унікальних символів:", len(counts))

print("Повторювані символи:")
found = False
for char in counts:
    if counts[char] > 1:
        print(f"{char}: {counts[char]}")
        found = True

if not found:
    print("Немає символів, що повторюються.")