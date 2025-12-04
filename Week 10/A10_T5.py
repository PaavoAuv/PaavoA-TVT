########################################################
# Task A10_T5
# Developer: Paavo Auvinen
# Date: 2025-12-04
########################################################

def recursiveFactorial(PNum: int) -> int:
    """
    Recursively calculates factorial of PNum.
    0! and 1! are defined as 1.
    """
    if PNum <= 1:
        return 1
    return PNum * recursiveFactorial(PNum - 1)


def main() -> None:
    print("Program starting.")
    user_input = input("Insert factorial: ")
    try:
        num = int(user_input)
        if num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            result = recursiveFactorial(num)
            print(f"Factorial {num}!")
            print(f"{num} = {result}")
    except ValueError:
        print("Invalid input. Please insert an integer.")
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
