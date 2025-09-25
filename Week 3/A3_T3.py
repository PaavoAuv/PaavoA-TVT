print("Program starting.")


name = input("Insert your username: ")


print("\nMenu:")
print("1. Print welcome message")
print("2. Exit")


choice = input("Your choice: ")


if choice == "1":
    print(f"Welcome {name}!")
elif choice == "2":
    print("Exiting...")
else:
    print("Unknown option.")

print("Program ending.")