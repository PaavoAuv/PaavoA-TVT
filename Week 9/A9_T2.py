import sys

print("Program starting.")

raw = input("Insert exit code(0-255): ")

try:
    code = int(raw)
except ValueError:
    print("Invalid input, must be an integer.")
    sys.exit(1)

if code < 0 or code > 255:
    print("Invalid input, must be between 0 and 255.")
    sys.exit(1)

if code == 0:
    print("Clean exit")

sys.exit(code)
