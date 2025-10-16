def askName():
    pName = input("Insert name: ")
    return pName


def greetUser(pName):
    print(f"Hello {pName}!")
    return None


def main():
    print("Program starting.")
    pName = askName()
    greetUser(pName)
    print("Program ending.")
    return None


main()
