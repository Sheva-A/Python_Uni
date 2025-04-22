celsius = [0, 10, 20, 30, 40, 100]

fahrenheit = [temp * 9/5 + 32 for temp in celsius]

print(f"Температури у Фаренгейтах: {fahrenheit}")