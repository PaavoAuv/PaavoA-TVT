import time

def print_menu():
    print("Options:")
    print("1---Set pause duration")
    print("2---Activate pause")
    print("0---Exit")

def main():
    print("Program starting.")
    pause_duration = 1.0  # default value

    while True:
        print_menu()
        choice = input("Your choice: ")

        if choice == "1":
            new_value = input("Insert pause duration (s): ")
            try:
                pause_duration = float(new_value)
            except ValueError:
                print("Invalid value.")
        elif choice == "2":
            print(f"Pausing for {pause_duration} seconds.")
            time.sleep(pause_duration)
            print("Unpaused.")
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")

    print("Program ending.")

main()
