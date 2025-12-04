########################################################
# Task A10_T2
# Developer: Paavo Auvinen
# Date: 2025-12-04
########################################################

import sys


def readValues(PFilename: str, PValues: list[int]) -> None:
    """
    Reads integers from the given file and appends them to PValues.
    Ignores empty rows and strips newline characters.
    Exits the program if the file cannot be opened or a value is invalid.
    """
    try:
        with open(PFilename, "r") as file:
            for row in file:
                clean = row.strip()
                if clean != "":
                    try:
                        number = int(clean)
                        PValues.append(number)
                    except ValueError:
                        print("Error: file contains a non-integer value.")
                        sys.exit(1)
    except FileNotFoundError:
        print("Error: file not found.")
        sys.exit(1)
    return None


def sumOfValues(PValues: list[int]) -> int:
    """
    Calculates and returns the sum of values in PValues.
    """
    total: int = 0
    for value in PValues:
        total += value
    return total


def productOfValues(PValues: list[int]) -> int:
    """
    Calculates and returns the product of values in PValues.
    """
    product: int = 1
    for value in PValues:
        product *= value
    return product


def main() -> None:
   
    Values: list[int] = []

    
    print("Program starting.")
    filename: str = input("Insert filename: ")

    readValues(filename, Values)

    
    total_sum: int = sumOfValues(Values)

   
    total_product: int = productOfValues(Values)

    
    print("# --- Sum of numbers --- #")
    print(total_sum)
    print("# --- Sum of numbers --- #")
    print("# --- Product of numbers --- #")
    print(total_product)
    print("# --- Product of numbers --- #")

    
    Values.clear()
    print("Program ending.")
    return None


main()
