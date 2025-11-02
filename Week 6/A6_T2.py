
def main():
    print("Program starting.")
    first = input("Insert first name: ").strip()
    last = input("Insert last name: ").strip()
    filename = input("Insert filename: ").strip()

    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(first + "\n")
            f.write(last + "\n")
           
            f.write("\n")
    except OSError as e:
        print(f"Error writing file: {e}")

    print("Program ending.")

if __name__ == "__main__":
    main()
