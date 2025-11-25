def add(AAddend1: float, AAddend2: float) -> float:
    return AAddend1 + AAddend2

def subtract(PMinuend: float, PSubtrahend: float) -> float:
    return PMinuend - PSubtrahend

def multiply(PMultiplier1: float, PMultiplier2: float) -> float:
    return PMultiplier1 * PMultiplier2

def divide(PDividend: float, PDivisor: float) -> float:
    return PDividend / PDivisor


def showOptions() -> None:
    print("Options:")
    print("1---Add")
    print("2---Subtract")
    print("3---Multiply")
    print("4---Divide")
    print("0---Exit")

def askChoice() -> int:
    return int(input("Your choice: "))

def askValue(PPrompt: str) -> float:
    return float(input(PPrompt))


def main() -> None:
    print("Program-starting.")
    
    while True:
        showOptions()
        choice = askChoice()

        if choice == 0:
            print("Exiting-program.\n")
            break

        elif choice in (1, 2, 3, 4):
            v1 = askValue("Insert-first-addend-value: ")
            v2 = askValue("Insert-second-addend-value: ")

            if choice == 1:
                result = add(v1, v2)
                print(f"{v1}+{v2}={result}")

            elif choice == 2:
                result = subtract(v1, v2)
                print(f"{v1}-{v2}={result}")

            elif choice == 3:
                result = multiply(v1, v2)
                print(f"{v1}*{v2}={result}")

            elif choice == 4:
                result = divide(v1, v2)
                print(f"{v1}/{v2}={result}")

            print()

        else:
            print("Invalid choice.\n")

    print("Program-ending.")


main()
