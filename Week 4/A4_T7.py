

print("Program.starting.\n")

print("Check.multiplicative.persistency.")
n = int(input("Insert.an.integer.: "))

steps = 0

while n >= 10:
    s = str(n)
    print(s, end=" -> ")
    product = 1
    for ch in s:
        product *= int(ch)
        print(ch, end="*")
    print("\b= ", end="")  # remove last '*' and add '='
    print(product)
    n = product
    steps += 1

print("No.more.steps.\n")
print(f"This.program.took.{steps}.step(s)\n")
print("Program.ending.")
