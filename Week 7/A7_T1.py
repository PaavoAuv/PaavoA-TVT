

def main():
    print("Program starting.")
    print("Collect positive integers.")

    numbers: list[int] = []

    while True:
        try:
            num = int(input("Insert positive integer(negative stops): "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if num < 0:
            print("Stopped collecting positive integers.")
            break
        elif num > 0:
            numbers.append(num)
        else:
           
            print("Zero is not a positive integer, ignoring.")
    
    if len(numbers) == 0:
        print("No positive integers were entered.")
    else:
        print(f"Displaying {len(numbers)} integers:")
        for index, value in enumerate(numbers):
            ordinal = index + 1
            print(f"- Index {index} => Ordinal {ordinal} => Integer {value}")

    print("Program ending.")


if __name__ == "__main__":
    main()
