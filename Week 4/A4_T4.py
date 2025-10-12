

print("Program.starting.\n")

words = []
while True:
    word = input("Insert word (empty=stops): ")
    if word == "":
        break
    words.append(word)

print("\nYou inserted:")
print(len(words), "words")
print(sum(len(w) for w in words), "characters")

print("\nProgram.ending.")
