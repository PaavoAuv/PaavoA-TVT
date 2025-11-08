

import os


WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday",)

def readFile(PFilename: str, PRows: list[str]) -> None:
    
    base_path = os.path.dirname(__file__)
    full_path = os.path.join(base_path, PFilename)

    print(f'Reading file "{full_path}".')
    PRows.clear()

   
    if not os.path.exists(full_path):
        print(f'Error: File "{full_path}" not found.')
        return None

    
    with open(full_path, "r", encoding="utf-8-sig") as file:
        header_skipped = False
        for line in file:
            if not header_skipped:
                header_skipped = True
                continue  # skip header row

            line = line.strip()
            if line == "":
                continue

            
            line = line.replace("\ufeff", "").strip()
            PRows.append(line)

    if len(PRows) == 0:
        print("Warning: File was read successfully but contained no data rows.")
    return None


def analyseTimestamps(PRows: list[str], PResults: list[str]) -> None:
    print("Analysing timestamps.")
    PResults.clear()

    WeekdayTimestampAmount = [0] * 7

    for row in PRows:
        first_column = row.split(";")[0].strip()
        for i, day in enumerate(WEEKDAYS):
            if first_column == day:
                WeekdayTimestampAmount[i] += 1
                break

    PResults.append("### Timestamp analysis ###")
    for i, day in enumerate(WEEKDAYS):
        PResults.append(f" - {day} {WeekdayTimestampAmount[i]} stamps")
    PResults.append("### Timestamp analysis ###")

    return None


def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    for line in PResults:
        print(line)
    return None


def main() -> None:
    print("Program starting.")

    Rows: list[str] = []
    Results: list[str] = []

    filename = input("Insert filename: ").strip()
    readFile(filename, Rows)

    if len(Rows) == 0:
        print("No data rows to analyze — please check the file.")
    else:
        analyseTimestamps(Rows, Results)
        displayResults(Results)

    Rows.clear()
    Results.clear()

    print("Program ending.")
    return None



main()
