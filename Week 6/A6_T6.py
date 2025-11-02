LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def shiftCharacter(Character: str, Alphabets: str, Shift: int = 13) -> str:
    """Shifts a character by `Shift` positions in the given alphabet."""
    if Character in Alphabets:
        index = Alphabets.index(Character)
        new_index = (index + Shift) % 26
        return Alphabets[new_index]
    return Character


def rot13(Content: str) -> str:
    """Applies ROT13 cipher to the input string."""
    result = ""
    for ch in Content:
        if ch in LOWER_ALPHABETS:
            result += shiftCharacter(ch, LOWER_ALPHABETS)
        elif ch in UPPER_ALPHABETS:
            result += shiftCharacter(ch, UPPER_ALPHABETS)
        else:
            result += ch
    return result


def askRows() -> str:
    """Asks the user to input multiple lines until an empty line is entered."""
    print("Collecting plain text rows for ciphering.")
    rows = []
    while True:
        row = input("Insert row(empty stops): ")
        if row == "":
            break
        rows.append(row)
    return "\n".join(rows)


def writeFile(Filename: str, Content: str) -> None:
    """Saves the encrypted text to a file if filename is given."""
    if Filename.strip() == "":
        print("File name not defined.")
        print("Aborting save operation.")
        return
    with open(Filename, "w", encoding="utf-8") as f:
        f.write(Content)
    print("Ciphered text saved!")


def main():
    print("Program starting.\n")
    content = askRows()

    ciphered = rot13(content)
    print("\n#### Ciphered text ####")
    print(ciphered)
    print("\n#### Ciphered text ####")
    filename = input("Insert filename to save: ")

    if filename.strip() == "":
        print("File name not defined.")
        print("Aborting save operation.")
    else:
        writeFile(filename, ciphered)
    print("Program ending.")


if __name__ == "__main__":
    main()
