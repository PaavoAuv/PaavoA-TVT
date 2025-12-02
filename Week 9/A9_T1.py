print("Program starting.\n")

total = 0.0

while True:
    raw = input("Insert a floating-point value (0 to stop): ")

    try:
        value = float(raw)
    except ValueError:
        print("Error! '{}' couldn't be converted to float.".format(raw))
        continue

    if value == 0:
        break

    total += value

print("\nFinal sum is {:.2f}".format(total))
print("Program ending.")
