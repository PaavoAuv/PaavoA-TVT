
def main():
    print("Program starting.")
    print("This program can copy a file.")
    src = input("Insert source filename: ").strip()
    dst = input("Insert destination filename: ").strip()

    try:
        print(f"Reading file '{src}' content.")
        with open(src, "r", encoding="utf-8") as fsrc:
            data = fsrc.read()
        print("File content ready in memory.")
        print(f"Writing content into file '{dst}'.")
        with open(dst, "w", encoding="utf-8") as fdst:
            fdst.write(data)
        print("Copying operation complete.")
    except FileNotFoundError:
        print(f"Error: file '{src}' not found.")
    except OSError as e:
        print(f"File error: {e}")

    print("Program ending.")

if __name__ == "__main__":
    main()
