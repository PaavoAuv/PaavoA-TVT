import os

def show_options():
    print("Options:")
    print("1---Read-values")
    print("2---Amount-of-values")
    print("3---Calculate-sum-of-values")
    print("4---Calculate-average-of-values")
    print("0---Exit")


def read_values():
    filename = input("Insert-filename: ").strip()
    values = []

   
    base_dir = os.path.dirname(__file__)
    full_path = os.path.join(base_dir, filename)

    with open(full_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            values.append(float(line))

    print() 
    return values


def amount_of_values(values):
    print(f"Amount-of-values:{len(values)}")
    print()


def sum_of_values(values):
    if not values:
        total = 0.0
    else:
        total = sum(values)
    # yksi desimaali
    print(f"Sum-of-values:{total:.1f}")
    print()


def average_of_values(values):
    if not values:
        avg = 0.0
    else:
        avg = sum(values) / len(values)
    print(f"Average-of-values:{avg:.1f}")
    print()


def main():
    print("Program-starting.")

    values = []

    while True:
        show_options()
        choice = input("Your-choice: ").strip()

        if choice == "0":
            print("Exiting-program.")
            print()
            break
        elif choice == "1":
            values = read_values()
        elif choice == "2":
            amount_of_values(values)
        elif choice == "3":
            sum_of_values(values)
        elif choice == "4":
            average_of_values(values)
        else:
            print()

    print("Program-ending.")


main()
