def showMenu():
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Decrease count")
    print("4 - Reset count")
    print("0 - Exit")
    return None


def main():
    print("Program starting.")
    count = 0

    while True:
        showMenu()
        choice = input("Your choice: ")

        if choice == "1":
            print(f"Count value: {count}")
        elif choice == "2":
            count += 1
            print("Count increased.")
        elif choice == "3":
            count -= 1
            print("Count decreased.")
        elif choice == "4":
            count = 0
            print("Count reset.")
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Unknown option.")
        print()

    print("Program ending.")
    return None


main()
