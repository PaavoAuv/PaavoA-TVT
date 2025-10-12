print("Program starting.")

# Main menu
print("\nMenu:")
print("1. Length")
print("2. Weight")
print("3. Exit")

choice = input("Your choice: ")

if choice == "1":
   
    print("\nLength conversions:")
    print("1. Meters to kilometers")
    print("2. Kilometers to meters")
    sub_choice = input("Your choice: ")

    if sub_choice == "1":
        meters = float(input("Insert meters: "))
        kilometers = meters / 1000
        print(f"{kilometers:.1f} km")
    elif sub_choice == "2":
        kilometers = float(input("Insert kilometers: "))
        meters = kilometers * 1000
        print(f"{meters:.1f} m")
    else:
        print("Unknown option.")

elif choice == "2":
    
    print("\nWeight conversions:")
    print("1. Grams to pounds")
    print("2. Pounds to grams")
    sub_choice = input("Your choice: ")

    if sub_choice == "1":
        grams = float(input("Insert grams: "))
        pounds = grams / 453.59237
        print(f"{pounds:.1f} lb")
    elif sub_choice == "2":
        pounds = float(input("Insert pounds: "))
        grams = pounds * 453.59237
        print(f"{grams:.1f} g")
    else:
        print("Unknown option.")

elif choice == "3":
    print("Exiting...")

else:
    print("Unknown option.")

print("Program ending.")
