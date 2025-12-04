########################################################
# Task A10_T6
# Developer: Paavo Auvinen
# Date: 2025-12-04
########################################################

import copy
import time
from typing import Callable


def readValues(PValues: list[int]) -> str:
    """
    Reads integer values from a text file into PValues.
    Asks for filename, clears existing list first.
    Returns the dataset filename (for printing in results).
    """
    PValues.clear()
    filename = input("Insert dataset filename: ")
    try:
        with open(filename, "r", encoding="utf-8") as fh:
            for line in fh:
                clean = line.strip()
                if clean != "":
                    PValues.append(int(clean))
    except FileNotFoundError:
        print("Error: file not found.")
    except ValueError:
        print("Error: file contains non-integer values.")
        PValues.clear()
    return filename


def bubbleSort(PNums: list[int]) -> list[int]:
    """
    Bubble sort implementation (in-place, ascending).
    Returns the sorted list (same object).
    """
    n = len(PNums)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if PNums[j] > PNums[j + 1]:
                PNums[j], PNums[j + 1] = PNums[j + 1], PNums[j]
    return PNums


def _quickSortHelper(PNums: list[int], low: int, high: int) -> None:
    if low >= high:
        return
    pivot = PNums[high]
    i = low - 1
    for j in range(low, high):
        if PNums[j] <= pivot:
            i += 1
            PNums[i], PNums[j] = PNums[j], PNums[i]
    i += 1
    PNums[i], PNums[high] = PNums[high], PNums[i]
    _quickSortHelper(PNums, low, i - 1)
    _quickSortHelper(PNums, i + 1, high)


def quickSort(PNums: list[int]) -> list[int]:
    """
    Quicksort implementation (in-place, ascending).
    Returns the sorted list (same object).
    """
    if len(PNums) > 1:
        _quickSortHelper(PNums, 0, len(PNums) - 1)
    return PNums


def measureSortingTime(PSortingAlgorithm: Callable, PArr: list[int]) -> int:
    """
    Measures nanoseconds spent by PSortingAlgorithm on PArr.
    PSortingAlgorithm is a callable that takes a list and sorts it.
    """
    start_time = time.perf_counter_ns()
    PSortingAlgorithm(PArr)
    end_time = time.perf_counter_ns()
    elapsed_time = end_time - start_time
    return elapsed_time


def main() -> None:
    
    Values: list[int] = []
    Results: list[str] = []
    current_dataset_name: str = ""

    
    print("Program starting.")

    while True:
        print("Options:")
        print("1 - Read dataset values")
        print("2 - Measure speeds")
        print("3 - Save results")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "1":
            current_dataset_name = readValues(Values)

        elif choice == "2":
            if not Values:
                print("No dataset loaded. Use option 1 first.")
            else:
                
                builtin_time = measureSortingTime(sorted, copy.deepcopy(Values))
                bubble_time = measureSortingTime(bubbleSort, copy.deepcopy(Values))
                quick_time = measureSortingTime(quickSort, copy.deepcopy(Values))

                result = (
                    f"Measured speeds for dataset '{current_dataset_name}':\n"
                    f" - Built-in sorted {builtin_time} ns\n"
                    f" - Buble sort {bubble_time} ns\n"
                    f" - Quick sort {quick_time} ns\n"
                )
                print(result.strip())  
                print()  

                Results.append(result)

        elif choice == "3":
            if not Results:
                print("No results to save. Measure speeds first.")
            else:
                filename = input("Insert results filename: ")
                try:
                    with open(filename, "w", encoding="utf-8") as fh:
                        for res in Results:
                            fh.write(res)
                            if not res.endswith("\n"):
                                fh.write("\n")
                    print(f"Results saved to '{filename}'.")
                except OSError:
                    print("Error: could not write results file.")

        elif choice == "0":
            print("Exiting program.")
            break

        else:
            print("Invalid choice.")

        print()  

    
    Values.clear()
    Results.clear()
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
