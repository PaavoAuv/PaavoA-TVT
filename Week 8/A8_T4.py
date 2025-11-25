from datetime import datetime
import os

# Constant month and weekday names
MONTHS = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
)

WEEKDAYS = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
)


def readTimestamps(PFilename: str, PTimestamps: list[datetime]) -> None:
    """Read timestamps from given file and append them to PTimestamps."""
    # Always read from the same folder where this .py file is
    script_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(script_dir, PFilename)

    with open(full_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            # Format in file: 2000-04-11T05:01
            dt = datetime.strptime(line, "%Y-%m-%dT%H:%M")
            PTimestamps.append(dt)


def calculateYears(PYear: int, PTimestamps: list[datetime]) -> int:
    """Return amount of timestamps with given year."""
    count = 0
    for ts in PTimestamps:
        if ts.year == PYear:
            count += 1
    return count


def calculateMonths(PMonth: str, PTimestamps: list[datetime]) -> int:
    """Return amount of timestamps occurring in the given month name."""
    if PMonth:
        month_norm = PMonth[0].upper() + PMonth[1:].lower()
    else:
        month_norm = ""

    if month_norm not in MONTHS:
        return 0

    month_index = MONTHS.index(month_norm) + 1  # datetime month is 1–12
    count = 0
    for ts in PTimestamps:
        if ts.month == month_index:
            count += 1
    return count


def calculateWeekdays(PWeekday: str, PTimestamps: list[datetime]) -> int:
    """Return amount of timestamps occurring on the given weekday name."""
    if PWeekday:
        weekday_norm = PWeekday[0].upper() + PWeekday[1:].lower()
    else:
        weekday_norm = ""

    if weekday_norm not in WEEKDAYS:
        return 0

    weekday_index = WEEKDAYS.index(weekday_norm)  # Monday = 0
    count = 0
    for ts in PTimestamps:
        if ts.weekday() == weekday_index:
            count += 1
    return count


def show_menu() -> None:
    print("Options:")
    print("1 - Calculate amount of timestamps during year")
    print("2 - Calculate amount of timestamps during month")
    print("3 - Calculate amount of timestamps during weekday")
    print("0 - Exit")


def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ").strip()

    timestamps: list[datetime] = []
    readTimestamps(filename, timestamps)

    while True:
        show_menu()
        choice = input("Your choice: ").strip()

        if choice == "0":
            print("Exiting program.")
            print()
            break

        elif choice == "1":
            year_str = input("Insert year: ").strip()
            try:
                year = int(year_str)
            except ValueError:
                print("Invalid year.")
                print()
                continue

            amount = calculateYears(year, timestamps)
            print(f"Amount of timestamps during year '{year}' is {amount}")
            print()

        elif choice == "2":
            month_input = input("Insert month: ").strip()
            if month_input:
                month_print = month_input[0].upper() + month_input[1:].lower()
            else:
                month_print = ""

            amount = calculateMonths(month_input, timestamps)
            print(f"Amount of timestamps during month '{month_print}' is {amount}")
            print()

        elif choice == "3":
            weekday_input = input("Insert weekday: ").strip()
            if weekday_input:
                weekday_print = weekday_input[0].upper() + weekday_input[1:].lower()
            else:
                weekday_print = ""

            amount = calculateWeekdays(weekday_input, timestamps)
            print(f"Amount of timestamps during weekday '{weekday_print}' is {amount}")
            print()

        else:
            print("Invalid choice.")
            print()

    print("Program ending.")


if __name__ == "__main__":
    main()
