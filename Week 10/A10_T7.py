########################################################
# Task A10_T7
# Developer: Paavo Auvinen
# Date: 2025-12-04
########################################################

import random

random.seed(1234)


def layMines(PMineField: list[list[int]], PMines: int) -> None:
    """
    Randomly places mines (value 9) into the existing 2D matrix PMineField.
    Does not change dimensions, only values 0 -> 9 at mine locations.
    """
    if not PMineField or not PMineField[0]:
        return None

    rows = len(PMineField)
    cols = len(PMineField[0])
    max_cells = rows * cols
    mines_to_place = min(PMines, max_cells)

    placed = 0
    while placed < mines_to_place:
        r = random.randrange(rows)
        c = random.randrange(cols)
        if PMineField[r][c] != 9:
            PMineField[r][c] = 9
            placed += 1

    return None


def calculateNearbys(PMineField: list[list[int]]) -> None:
    """
    Expects 2D matrix with mines (9) already placed.
    For each non-mine cell, calculates number of nearby mines in 8 directions.
    Modifies PMineField in-place.
    """
    if not PMineField or not PMineField[0]:
        return None

    rows = len(PMineField)
    cols = len(PMineField[0])

    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]

    for r in range(rows):
        for c in range(cols):
            if PMineField[r][c] == 9:
                continue  
            count = 0
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if PMineField[nr][nc] == 9:
                        count += 1
            PMineField[r][c] = count

    return None


def generateMinefield(
    PMineField: list[list[int]],
    PRows: int,
    PCols: int,
    PMines: int
) -> None:
    """
    Takes empty PMineField list and amount of rows, columns and mines as parameters.
    1. Clear 2D-Matrix
    2. Initializes PMineField list with zeros using PRows and PCols
    3. Lay mines
    4. Calculate nearbys
    """
    PMineField.clear()

    
    for i in range(PRows):
        PMineField.append([])
        for _ in range(PCols):
            PMineField[i].append(0)

    
    layMines(PMineField, PMines)
    calculateNearbys(PMineField)

    return None


def main() -> None:
    """
    Menu-driven program to generate and manage minesweeper boards.
    """
    MineField: list[list[int]] = []

    print("Program starting.")

    while True:
        print("Options:")
        print("1 - Generate minesweeper board")
        print("2 - Show generated board")
        print("3 - Save generated board")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "1":
            try:
                rows = int(input("Insert rows: "))
                cols = int(input("Insert columns: "))
                mines = int(input("Insert mines: "))
                if rows <= 0 or cols <= 0 or mines < 0:
                    print("Rows and columns must be positive, mines non-negative.")
                else:
                    generateMinefield(MineField, rows, cols, mines)
            except ValueError:
                print("Invalid input. Please insert integer values.")

        elif choice == "2":
            if not MineField:
                print("No board generated yet.")
            else:
                for row in MineField:
                    print(row)

        elif choice == "3":
            if not MineField:
                print("No board generated to save.")
            else:
                filename = input("Insert filename: ")
                try:
                    with open(filename, "w", encoding="utf-8") as fh:
                        for row in MineField:
                            line = ",".join(str(v) for v in row)
                            fh.write(line + "\n")
                    print(f"Board saved to '{filename}'.")
                except OSError:
                    print("Error: could not write file.")

        elif choice == "0":
            print("Exiting program.")
            break

        else:
            print("Invalid choice.")

        print()  

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
