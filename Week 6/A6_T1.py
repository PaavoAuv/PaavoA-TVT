
def main():
    print("Program starting.")
    print("This program can read a file.")
    filename = input("Insert filename: ").strip()

    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        print(f'#### START "{filename}" ####')
       
        print(content, end="" if content.endswith("\n") else "\n")
        print(f'#### END "{filename}" ####')
    except FileNotFoundError:
        print(f'Error: file "{filename}" not found.')
    except OSError as e:
        print(f"Error reading file: {e}")

    print("Program ending.")

if __name__ == "__main__":
    main()
