import sys
import os

def showHelp() -> None:
    print("Invalid amount of arguments.")
    print("Usage: python A9_T7.py <src_file> <dst_file>")


def copyFile(PSrcFile: str, PDstFile: str) -> None:
    Proceed = True

    print('Source file "{}"'.format(PSrcFile))
    print('Destination file "{}"'.format(PDstFile))

    # Check if destination file exists
    if os.path.exists(PDstFile):
        answer = input('Destination file "{}" exists. Overwrite (y/n)?: '.format(PDstFile))
        if answer.lower() != "y":
            Proceed = False
            print("Copy aborted by user.")

    if Proceed:
        try:
            print('Copying file "{}" to "{}".'.format(PSrcFile, PDstFile))
            with open(PSrcFile, "r", encoding="UTF-8") as src:
                data = src.read()
            with open(PDstFile, "w", encoding="UTF-8") as dst:
                dst.write(data)
        except Exception as e:
            print("Error: could not copy file. ({})".format(e))
            sys.exit(-1)


def main() -> None:
    print("Program starting.")

    # Expect exactly 3 arguments: script, src, dst
    if len(sys.argv) != 3:
        showHelp()
        print("Program ending.")
        return

    SrcFile = sys.argv[1]
    DstFile = sys.argv[2]

    copyFile(SrcFile, DstFile)

    print("Program ending.")


if __name__ == "__main__":
    main()
