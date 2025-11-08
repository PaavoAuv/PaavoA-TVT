
def main():
    print("Program starting.")

  
    user_input = input("Insert comma separated integers: ")

    
    parts = user_input.split(",")

    
    valid_integers: list[int] = []

    
    for item in parts:
        item = item.strip()  
        if item == "":
            
            continue
        try:
            num = int(item)
            valid_integers.append(num)
        except ValueError:
            print(f"Error: '{item}' is not a valid integer.")

    
    if len(valid_integers) == 0:
        print("No valid integers to analyze.")
        print("Program ending.")
        return

  
    total_sum = sum(valid_integers)

    if total_sum % 2 == 0:
        parity = "even"
    else:
        parity = "odd"

    print(f"There are {len(valid_integers)} integers in the list.")
    print(f"Sum of the integers is {total_sum} and it's {parity}")

    print("Program ending.")


if __name__ == "__main__":
    main()
