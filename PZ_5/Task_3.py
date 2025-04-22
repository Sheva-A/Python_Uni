age = int(input("Enter your age: "))
experience = int(input("Enter the number of years of work experience: "))
qualification = bool(input("Are you qualified? (True/False): "))

if (25 <= age <= 50) and (experience > 3 or qualification):
    print("The candidate meets the requirements.")
else:
    print("The candidate does not meet the requirements.")