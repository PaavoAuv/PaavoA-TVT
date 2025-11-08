

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def load_config(filename: str) -> tuple[list[str], str]:
    """Load rotor and reflector configuration from file."""
    rotors = []
    reflector = ""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line.startswith("Rotor1:"):
                    rotors.append(line.split(":")[1].strip())
                elif line.startswith("Rotor2:"):
                    rotors.append(line.split(":")[1].strip())
                elif line.startswith("Rotor3:"):
                    rotors.append(line.split(":")[1].strip())
                elif line.startswith("Reflector:"):
                    reflector = line.split(":")[1].strip()
    except FileNotFoundError:
        print(f'Error: Configuration file "{filename}" not found.')
        exit(1)
    return rotors, reflector


def rotate_positions(positions: list[int]) -> None:
    """Rotate rotor positions like real Enigma: right rotor every press, carry over when wraps."""
    positions[0] = (positions[0] + 1) % 26
    if positions[0] == 0:
        positions[1] = (positions[1] + 1) % 26
        if positions[1] == 0:
            positions[2] = (positions[2] + 1) % 26
    return None


def scramble_forward(letter: str, rotors: list[str], positions: list[int]) -> str:
    """Forward pass through 3 rotors."""
    index = ALPHABET.index(letter)
    for i in range(3):
        shifted = (index + positions[i]) % 26
        letter = rotors[i][shifted]
        index = ALPHABET.index(letter)
    return letter


def scramble_reflector(letter: str, reflector: str) -> str:
    """Reflector substitution."""
    idx = ALPHABET.index(letter)
    return reflector[idx]


def scramble_reverse(letter: str, rotors: list[str], positions: list[int]) -> str:
    """Reverse pass through 3 rotors."""
    index = ALPHABET.index(letter)
    for i in range(2, -1, -1):
        shifted = (index - positions[i]) % 26
        letter = ALPHABET[rotors[i].index(ALPHABET[shifted])]
        index = ALPHABET.index(letter)
    return letter


def enigma_encrypt(text: str, rotors: list[str], reflector: str) -> str:
    """Encrypt or decrypt a text string."""
    positions = [0, 0, 0]  
    result = ""
    for ch in text:
        if ch not in ALPHABET:
            continue
        rotate_positions(positions)
        step1 = scramble_forward(ch, rotors, positions)
        step2 = scramble_reflector(step1, reflector)
        step3 = scramble_reverse(step2, rotors, positions)
        print(f'Character "{ch}" illuminated as "{step3}"')
        result += step3
    print(f'Converted row - "{result}".\n')
    return result


def main() -> None:
    print("Insert config(filename): ", end="")
    conf_file = input().strip()
    rotors, reflector = load_config(conf_file)

    plug = input("Insert plugs (y/n)?: ").strip().lower()
    if plug == "y":
        print("Plugboard feature not implemented.")
    else:
        print("No extra plugs inserted.")

    print("Enigma initialized.\n")

    while True:
        text = input("Insert row (empty stops): ").strip().upper()
        if text == "":
            print("\nEnigma closing.")
            break
        enigma_encrypt(text, rotors, reflector)



if __name__ == "__main__":
    main()
