

import os


DELIMITER = ";"
WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday",)


class TIMESTAMP:
    def __init__(self):
        self.weekday: str = ""
        self.hour: str = ""
        self.consumption: float = 0.0
        self.price: float = 0.0


class DAY_USAGE:
    def __init__(self, weekday: str):
        self.weekday: str = weekday
        self.total_consumption: float = 0.0
        self.total_cost: float = 0.0


def readFile(PFilename: str, PTimestamps: list['TIMESTAMP']) -> None:
    """Read the CSV file and populate timestamp list."""
    
    base_path = os.path.dirname(__file__)
    full_path = os.path.join(base_path, PFilename)

    print(f'Reading file "{PFilename}".')
    PTimestamps.clear()

    
    if not os.path.exists(full_path):
        print(f'Error: File "{PFilename}" not found.')
        return None

    with open(full_path, "r", encoding="utf-8-sig") as file:
        header_skipped = False
        for line in file:
            if not header_skipped:
                header_skipped = True
                continue  

            line = line.strip()
            if line == "":
                continue

            columns = line.split(DELIMITER)
            if len(columns) < 4:
                continue

            ts = TIMESTAMP()
            ts.weekday = columns[0].strip()
            ts.hour = columns[1].strip()
            ts.consumption = float(columns[2].strip())
            ts.price = float(columns[3].strip())
            PTimestamps.append(ts)

    return None


def analyseTimestamps(PTimestamps: list['TIMESTAMP'], PDayUsage: list['DAY_USAGE'], PResults: list[str]) -> None:
    """Analyse daily usage and fill result list."""
    print("Analysing timestamps.")
    PResults.clear()
    PDayUsage.clear()

   
    for day in WEEKDAYS:
        PDayUsage.append(DAY_USAGE(day))

    
    for ts in PTimestamps:
        for day_usage in PDayUsage:
            if ts.weekday == day_usage.weekday:
                day_usage.total_consumption += ts.consumption
                day_usage.total_cost += ts.price * ts.consumption
                break

    
    PResults.append("### Electricity consumption summary ###")
    for day_usage in PDayUsage:
        PResults.append(
            f" - {day_usage.weekday} usage {day_usage.total_consumption:.2f} kWh, cost {day_usage.total_cost:.2f} €"
        )
    PResults.append("### Electricity consumption summary ###")

    return None


def displayResults(PResults: list[str]) -> None:
    """Display results."""
    print("Displaying results.")
    for line in PResults:
        print(line)
    return None


def main() -> None:
    print("Program starting.")

    timestamps: list[TIMESTAMP] = []
    day_usage: list[DAY_USAGE] = []
    results: list[str] = []

    filename = input("Insert filename: ").strip()
    readFile(filename, timestamps)
    analyseTimestamps(timestamps, day_usage, results)
    displayResults(results)

    timestamps.clear()
    day_usage.clear()
    results.clear()

    print("Program ending.")
    return None


main()
