SEPARATOR = ";"


def readValues(filename: str = None) -> str:
    if filename is None:
        filename = input("Insert filename: ")
    with open(filename, "r", encoding="utf-8") as f:
        rows = [line.strip() for line in f.read().splitlines()]
    return SEPARATOR.join(rows)


def analyseNumbers(values: str) -> str:
    nums = [int(x) for x in values.split(SEPARATOR) if x != ""]
    count = len(nums)
    total = sum(nums)
    greatest = max(nums) if nums else 0
    average = (total / count) if count else 0.0
    return f"{count};{total};{greatest};{average:.2f}"


def displayResults(filename: str, results: str) -> None:
    print("#### Number analysis - START ####")
    print(f'File "{filename}" results:')
    print("Count;Sum;Greatest;Average")
    print(results)
    print("\n#### Number analysis - END ####")


def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    values = readValues(filename)
    results = analyseNumbers(values)
    displayResults(filename, results)
    print("Program ending.")


if __name__ == "__main__":
    main()
