
import os


DELIMITER = ";"



class TIMESTAMP:
    def __init__(self):
        self.weekday: str = ""
        self.hour: str = ""
        self.consumption: float = 0.0
        self.price: float = 0.0


def readFile(PFilename: str, PTimestamps: list['TIMESTAMP']) -> None:
    """Reads timestamp data from CSV in the same folder."""
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


def displayData(PTimestamps: list['TIMESTAMP']) -> None:
    """Prints electricity usage per timestamp."""
    print("Electricity usage:")
    for ts in PTimestamps:
        total = ts.price * ts.consumption
        print(f" - {ts.weekday} {ts.hour}:00, price {ts.price:.2f}, "
              f"consumption {ts.consumption:.2f} kWh, total {total:.2f} €")
    return None


def main() -> None:
    print("Program starting.")
    timestamps: list[TIMESTAMP] = []

    filename = input("Insert filename: ").strip()
    readFile(filename, timestamps)

    if len(timestamps) > 0:
        displayData(timestamps)

    timestamps.clear()
    print("Program ending.")
    return None


main()
