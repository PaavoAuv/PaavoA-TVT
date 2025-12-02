

def saveLines(lines):
    """Ask for filename and save given lines to a file."""
    filename = input("Insert filename: ")
    with open(filename, "w", encoding="UTF-8") as f:
        f.writelines(lines)


def main():
    lines = []

    print("Program starting.")

    while True:
        try:
            print()
            print("Options:")
            print("1 - Insert line")
            print("2 - Save lines")
            print("0 - Exit")
            choice = input("Your choice: ")

            if choice == "1":
                text = input("Insert text: ")
                
                lines.append(text + "\n")

            elif choice == "2":
                if len(lines) == 0:
                    print("No lines to save.")
                else:
                    saveLines(lines)

            elif choice == "0":
                print("Program ending.")
                break

            else:
                print("Unknown option.")

        except KeyboardInterrupt:
      
            print("Keyboard interrupt and unsaved progress!")
            if len(lines) > 0:
                try:
                    answer = input("Save before quit(y/n)?: ")
                except KeyboardInterrupt:
                    
                    print()
                    print("Program ending.")
                    break

                if answer.lower() == "y":
                    saveLines(lines)
            
            print("Program ending.")
            break


if __name__ == "__main__":
    main()
