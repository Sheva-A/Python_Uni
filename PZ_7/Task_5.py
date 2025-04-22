bacteria = 10
rate = 20
limit = int(input("Максимальна кількість бактерій: "))
hours = 0

while bacteria < limit:
    print(f"Година {hours}: {int(bacteria)}")
    bacteria += bacteria * rate / 100
    hours += 1

print(f"Година {hours}: {int(bacteria)}")
print(f"Потрібно {hours} годин.")