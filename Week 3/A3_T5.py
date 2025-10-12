print("Program starting.")

# Print menu
print("\nMenu:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Exit")

# Ask for choice
choice = input("Your choice: ")

if choice == "1":
    # Celsius → Fahrenheit
    celsius = float(input("Insert temperature in Celsius: "))
    fahrenheit = (celsius * 1.8) + 32
    print(f"{fahrenheit:.1f} °F")

elif choice == "2":
    # Fahrenheit → Celsius
    fahrenheit = float(input("Insert temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) / 1.8
    print(f"{celsius:.1f} °C")

elif choice == "3":
    print("Exiting...")

else:
    print("Unknown option.")

print("Program ending.")
