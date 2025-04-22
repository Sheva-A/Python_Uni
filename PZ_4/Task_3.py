students = [
    ("Макс Кідрук", 88.5, 92),
    ("Лесь Курбас", 93.2, 98),
    ("Михайль Семенко", 76.4, 85),
    ("Василь Симоненко", 81.7, 90),
    ("Іларіон Павлюк", 69.5, 78)
]

print("-" * 60)
print("ЗВІТ ПРО УСПІШНІСТЬ СТУДЕНТІВ".center(60))
print("-" * 60)

print("{:<25}{:>15}{:^15}".format("Ім'я студента", "Сер. бал", "Відвідув. %"))
print("-" * 60)

total_grade = 0
total_attendance = 0

for name, grade, attendance in students:
    print("{:<25}{:>15.1f}{:^15}".format(name, grade, f"{attendance}%"))
    total_grade += grade
    total_attendance += attendance

avg_grade = total_grade / len(students)
avg_attendance = total_attendance / len(students)

print("-" * 60)
print("{:<25}{:>15.1f}{:^15}".format("Середні показники:", avg_grade, f"{avg_attendance:.1f}%"))