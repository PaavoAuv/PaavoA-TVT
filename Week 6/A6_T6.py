

ALPHABETS_LOWER = "abcdefghijklmnopqrstuvwxyz"
ALPHABETS_UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def writeFile(Filename: str, Content: str) -> None:
    """Writes the ciphered text to a file."""
    try:
        with open(Filename, "w", encoding="utf-8") as file:
            file.write(Content)
        print("Ciphered text saved!")
    except Exception:
        print("Error saving file.")
    return None


def askRows() -> str:
    """Asks the user to input multiple lines until empty line is entered."""
    print("Collecting plain text rows for ciphering.")
    rows = []
    while True:
        line = input("Insert row(empty stops): ")
        if line == "":
            break
        rows.append(line)
    return "\n".join(rows)


def shiftCharacter(Character: str, Alphabets: str, Shift: int = 13) -> str:
    """Shifts character by given amount inside the provided alphabet."""
    if Character not in Alphabets:
        return Character
    index = Alphabets.index(Character)
    shifted_index = (index + Shift) % 26
    return Alphabets[shifted_index]


def rot13(Content: str) -> str:
    """Applies ROT13 cipher to entire string."""
    result = ""
    for char in Content:
        if char.islower():
            result += shiftCharacter(char, ALPHABETS_LOWER)
        elif char.isupper():
            result += shiftCharacter(char, ALPHABETS_UPPER)
        else:
            result += char
    return result


def main() -> None:
    print("Program starting.\n")

    text = askRows()
    ciphered = rot13(text)

    print("\n#### Ciphered text ####")
    print(ciphered)
    print("\n#### Ciphered text ####")

    filename = input("Insert filename to save: ").strip()
    if filename == "":
        print("File name not defined.")
        print("Aborting save operation.")
    else:
        writeFile(filename, ciphered)

    print("Program ending.")
    return None


# Run program
main()
