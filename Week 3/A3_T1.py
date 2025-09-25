print("Program starting.")

# Step 1: Ask for two integers
print("Insert two integers.")
num1 = int(input("Insert first integer: "))
num2 = int(input("Insert second integer: "))

# Step 2: Compare the integers
print("Comparing inserted integers...")
if num1 == num2:
    print("Integers are the same.")
elif num1 > num2:
    print("First integer is greater.")
else:
    print("Second integer is greater.")

# Step 3: Create sum
print("\nAdding integers together")
total = num1 + num2
print(f"{num1} + {num2} = {total}")

# Step 4: Check parity (even/odd)
print("\nChecking the parity of the sum...")
if total % 2 == 0:
    print("Sum is even.")
else:
    print("Sum is odd.")

print("Program ending.")
