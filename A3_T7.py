print("Program starting.")

# Step 1: Prompt user for integer
value = int(input("Insert an integer: "))

# Step 2: Show menu
print("\nMenu:")
print("1. One multi-branched decision")
print("2. Independent if-statement decisions")
print("0. Exit")

choice = input("Your choice: ")

if choice == "1":
    print("\nApplying multi-branched decision...")
    if value >= 400:
        value += 44
    elif value >= 200:
        value += 22
    elif value >= 100:
        value += 11
    print(f"Resulting value is {value}")

elif choice == "2":
    print("\nApplying independent if-statement decisions...")
    if value >= 400:
        value += 44
    if value >= 200:
        value += 22
    if value >= 100:
        value += 11
    print(f"Resulting value is {value}")

elif choice == "0":
    print("Exiting...")

else:
    print("Unknown option.")

print("Program ending.")
