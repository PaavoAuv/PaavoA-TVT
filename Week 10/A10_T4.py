########################################################
# Task A10_T4
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
    On error, prints a message and returns an empty list.
    """
    values: list[int] = []
    try:
        with open(PFilename, "r", encoding="utf-8") as file:
            for row in file:
                clean = row.strip()
                if clean != "":
                    values.append(int(clean))
    except FileNotFoundError:
        print("Error: file not found:", PFilename)
    except ValueError:
        print("Error: file contains a non-integer value.")
    return values


def merge(PLeft: list[int], PRight: list[int], PMerge: list[int], PAsc: bool = True) -> None:
    """
    Merge two sorted lists (PLeft and PRight) into PMerge in-place.
    PAsc = True  -> ascending
    PAsc = False -> descending
    """
    i: int = 0  
    j: int = 0  
    k: int = 0  

    while i < len(PLeft) and j < len(PRight):
        left_val = PLeft[i]
        right_val = PRight[j]

        if PAsc:
            if left_val <= right_val:
                PMerge[k] = left_val
                i += 1
            else:
                PMerge[k] = right_val
                j += 1
        else:
            if left_val >= right_val:
                PMerge[k] = left_val
                i += 1
            else:
                PMerge[k] = right_val
                j += 1
        k += 1

    
    while i < len(PLeft):
        PMerge[k] = PLeft[i]
        i += 1
        k += 1

    while j < len(PRight):
        PMerge[k] = PRight[j]
        j += 1
        k += 1

    return None


def mergeSort(PValues: list[int], PAsc: bool = True) -> None:
    """
    Sort PValues in-place using merge sort.
    PAsc: True = ascending (default), False = descending.
    """
    length: int = len(PValues)
    if length <= 1:
        return None

    mid: int = length // 2
    left: list[int] = PValues[:mid]
    right: list[int] = PValues[mid:]

    
    mergeSort(left, PAsc)
    mergeSort(right, PAsc)

    
    merge(left, right, PValues, PAsc)
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

    
    mergeSort(values_asc, True)
    mergeSort(values_desc, False)

   
    print(f"Raw '{filename}' -> " + ", ".join(str(v) for v in values_raw))
    print(f"Ascending '{filename}' -> " + ", ".join(str(v) for v in values_asc))
    print(f"Descending '{filename}' -> " + ", ".join(str(v) for v in values_desc))

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
