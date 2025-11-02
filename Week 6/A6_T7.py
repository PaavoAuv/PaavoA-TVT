
import os

PROGRESS_FILE = "player_progress.txt"
HEADER = "current_location;next_location;passphrase"

INITIAL_ROW = "0;1;qvfpvcyvar"

PLACES = {
    0: "home",
    1: "Galba's palace",
    2: "Otho's palace",
    3: "Vitellius' palace",
    4: "Vespasian's palace",
}

LOWER = "abcdefghijklmnopqrstuvwxyz"
UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def rot13_char(c):
    if c in LOWER:
        return LOWER[(LOWER.index(c) + 13) % 26]
    if c in UPPER:
        return UPPER[(UPPER.index(c) + 13) % 26]
    return c

def rot13(s: str) -> str:
    return "".join(rot13_char(ch) for ch in s)

def ensure_progress_file():
    if not os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
            f.write(HEADER + "\n")
            f.write(INITIAL_ROW + "\n")

def read_last_progress():
    ensure_progress_file()
    last = None
    with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if line and line != HEADER:
                last = line
    if last is None:
    
        last = INITIAL_ROW
    parts = last.split(";")
    if len(parts) != 3:
        raise ValueError("Corrupt progress file.")
    cur, nxt, passphrase = int(parts[0]), int(parts[1]), parts[2]
    return cur, nxt, passphrase

def append_progress_line(line: str):
    with open(PROGRESS_FILE, "a", encoding="utf-8") as f:
        f.write(line.rstrip("\n") + "\n")

def main():
    print("Travel starting.")
    cur, nxt, passphrase = read_last_progress()

 
    print(f"Currently at {PLACES.get(cur, 'unknown')}.")
    print(f"Travelling to {PLACES.get(nxt, 'unknown')}...")
    print(f"...Arriving to the {PLACES.get(nxt, 'unknown')}.")
    print("Passing the guard at the entrance.")

   
    plain_pass = rot13(passphrase)
    print(f"\"{plain_pass.capitalize()}!\"")

    print("Looking for the message in the palace...")
    msg_filename = f"{nxt}_{passphrase}.gkg"
    try:
        with open(msg_filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
        if not lines:
            print("Ah, there it is! Seems cryptic, but it's empty?")
            print("[Game] Progress autosaved!")
            print("Deciphering Emperor's message...")
            print("Looks like I've got now the plain version copy of the Emperor's message.")
            print("Time to leave...")
            print("Travel ending.")
            return
        print("Ah, there it is! Seems cryptic.")

     
        first_cipher_line = lines[0].rstrip("\n")
        append_progress_line(first_cipher_line)

        print("[Game] Progress autosaved!")

    
        print("Deciphering Emperor's message...")
        plain_lines = [rot13(l.rstrip('\n')) for l in lines]
        out_plain = f"{nxt}-{plain_pass.lower()}.txt"
        with open(out_plain, "w", encoding="utf-8") as f:
            for pl in plain_lines:
                f.write(pl + "\n")

        print("Looks like I've got now the plain version copy of the Emperor's message.")
    except FileNotFoundError:
        print(f'Could not find "{msg_filename}". Place the palace file in the folder and re-run.')
    except OSError as e:
        print(f"File error: {e}")


    if nxt < 4:
        next_row = f"{nxt};{nxt+1};{passphrase}"
        append_progress_line(next_row)

    print("Time to leave...")
    print("Travel ending.")

if __name__ == "__main__":
    main()
