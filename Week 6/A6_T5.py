SEPARATOR = ";"


def readValues(filename: str) -> str:
    Values = ""
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            num = line.strip()
            Values += num
            if i < len(lines) - 1:
                Values += SEPARATOR
    return Values


def analyseNumbers(values: str) -> str:
    parts = values.split(SEPARATOR)
    numbers = [int(x) for x in parts if x.strip() != ""]
    Count = len(numbers)
    Sum_ = sum(numbers)
    Greatest = max(numbers)
    Average = Sum_ / Count
    result = f"{Count};{Sum_};{Greatest};{Average:.2f}"
    return result


def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    print("#### Number analysis - START ####")
    print(f'File "{filename}" results:')
    Values = readValues(filename)
    results = analyseNumbers(Values)
    print("Count;Sum;Greatest;Average")
    print(results)
    print("\n#### Number analysis - END ####")
    print("Program ending.")


if __name__ == "__main__":
    main()
