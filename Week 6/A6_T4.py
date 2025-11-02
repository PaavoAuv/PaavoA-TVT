
def analyze_names(lines):
    names = [line.strip() for line in lines if line.strip() != ""]
    count = len(names)
    if count == 0:
        return (0, 0, 0, 0.0)

    lengths = [len(n) for n in names]
    shortest = min(lengths)
    longest = max(lengths)
    avg = sum(lengths) / count
    return (count, shortest, longest, avg)

def main():
    print("Program starting.")
    print("This program analyses a list of names from a file.")
    fn = input("Insert filename to read: ").strip()
    try:
        print(f'Reading names from "{fn}".')
        with open(fn, "r", encoding="utf-8") as f:
            count, shortest, longest, avg = analyze_names(f.readlines())
        print("Analysing names...")
        print("Analysis complete!")
        print("#### REPORT BEGIN ####")
        print(f"Name count - {count}")
        print(f"Shortest name - {shortest} chars")
        print(f"Longest name - {longest} chars")
        print(f"Average name - {avg:.2f} chars")
        print("#### REPORT END ####")
    except FileNotFoundError:
        print(f'Error: file "{fn}" not found.')
    except OSError as e:
        print(f"File error: {e}")

    print("Program ending.")

if __name__ == "__main__":
    main()
