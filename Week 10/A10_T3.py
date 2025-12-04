########################################################
# Task A10_T3
# Developer: Paavo Auvinen
# Date: 2025-12-04
########################################################

import sys


def readValues(PFilename: str) -> list[int]:
    """
    Read integers from PFilename.
    - Strip newline characters
    - Ignore empty rows
    - Convert each line to int
    """
    values: list[int] = []
    try:
        with open(PFilename, "r") as file:
            for row in file:
                clean = row.strip()
                if clean != "":
                    number = int(clean)
                    values.append(number)
    except FileNotFoundError:
        print("Error: file not found.")
        sys.exit(1)
    except ValueError:
        print("Error: file contains a non-integer value.")
        sys.exit(1)
    return values


def bubbleSort(PValues: list[int], PAsc: bool = True) -> None:
    """
    Sort PValues in-place using bubble sort.
    - PAsc = True  -> ascending
    - PAsc = False -> descending
    Do not reassign PValues; modify elements via indices.
    """
    n: int = len(PValues)
    for i in range(n - 1):                 
        for j in range(0, n - i - 1):      
            current = PValues[j]
            nxt = PValues[j + 1]

            if PAsc:
                
                if current > nxt:
                    PValues[j], PValues[j + 1] = nxt, current
            else:
                
                if current < nxt:
                    PValues[j], PValues[j + 1] = nxt, current
    return None


def main() -> None:
    print("Program starting.")


    if len(sys.argv) == 2:
        filename: str = sys.argv[1]
    else:
        filename: str = input("Insert filename: ")

   
    values_raw: list[int] = readValues(filename)

    
    values_asc: list[int] = values_raw.copy()
    values_desc: list[int] = values_raw.copy()

    
    bubbleSort(values_asc, True)
    bubbleSort(values_desc, False)

   
    print(f"Raw '{filename}' -> " + ", ".join(str(v) for v in values_raw))
    print(f"Ascending '{filename}' -> " + ", ".join(str(v) for v in values_asc))
    print(f"Descending '{filename}' -> " + ", ".join(str(v) for v in values_desc))

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
