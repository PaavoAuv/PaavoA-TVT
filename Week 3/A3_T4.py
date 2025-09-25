print("Program starting.")

# Ask for username
name = input("Insert your username: ")

# Print menu
print("\nMenu:")
print("1. Print welcome message")
print("2. Exit")
print("3. Print the name backwards")
print("4. Print the first character")
print("5. Show the amount of characters in the name")

# Ask for choice
choice = input("Your choice: ")

# Perform action based on choice
if choice == "1":
    print(f"Welcome {name}!")
elif choice == "2":
    print("Exiting...")
elif choice == "3":
    print(f'Your name backwards is "{name[::-1]}"')
elif choice == "4":
    print(f'The first character in name "{name}" is "{name[0]}"')
elif choice == "5":
    print(f'There are {len(name)} characters in the name "{name}"')
else:
    print("Unknown option.")

print("Program ending.")