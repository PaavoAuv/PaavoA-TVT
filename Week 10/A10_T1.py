########################################################
# Task A10_T1
# Developer: Paavo Auvinen
# Date: 2025-12-04
########################################################

import os

def readValues(filename: str) -> list[str]:
    values: list[str] = []

    script_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(script_dir, filename)

    try:
        with open(full_path, "r") as file:
            for row in file:
                clean = row.strip()
                if clean != "":
                    values.append(clean)
    except FileNotFoundError:
        print("File not found:", full_path)
    return values


def displayVertically(values: list[str]) -> None:
    print("# --- Vertically --- #")
    for v in values:
        print(v)
    print("# --- Vertically --- #")


def displayHorizontally(values: list[str]) -> None:
    print("# --- Horizontally --- #")
    print(", ".join(values))
    print("# --- Horizontally --- #")


def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ")
    values = readValues(filename)

    if len(values) > 0:
        displayVertically(values)
        displayHorizontally(values)

    print("Program ending.")


main()
