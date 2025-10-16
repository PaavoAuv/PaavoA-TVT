def frameword(pWord):
    print('*' * (len(pWord) + 4))
    print(f'* {pWord} *')
    print('*' * (len(pWord) + 4))
    return None


def main():
    print("Program starting.")
    print()
    pWord = input("Insert word: ")
    print()
    frameword(pWord)
    print()
    print("Program ending.")
    return None



main()
