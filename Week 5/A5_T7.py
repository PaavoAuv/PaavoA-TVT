
DELIMITER = ','


def collectWords() -> str:
    words = []
    while True:
        word = input("Insert word (empty stops): ")
        if word == "":
            break
        words.append(word)
    return DELIMITER.join(words)


def analyseWords(words: str) -> None:
    if not words:
        print("No words entered.")
        return None

    word_list = words.split(DELIMITER)
    word_count = len(word_list)
    char_count = sum(len(word) for word in word_list)
    avg_length = char_count / word_count if word_count > 0 else 0

    print(f"- {word_count} Words")
    print(f"- {char_count} Characters")
    print(f"- {avg_length:.2f} Average word length")

    return None


def main():
    print("Program starting.")
    words = collectWords()
    analyseWords(words)
    print("Program ending.")
    return None



main()
