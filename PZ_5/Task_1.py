temperature = int(input("Enter temperature data: "))
humidity = int(input("Enter humidity data: "))

if temperature > 30 and humidity > 70:
    print("Activation of the cooling system.")
else:
    print("Conditions are normal.")