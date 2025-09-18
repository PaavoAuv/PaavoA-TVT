print("Program starting.")

name = input("What is your name: ")

num1 = float(input("Enter a floating point number: "))
num2 = float(input("Enter second floating point number: "))

product = num1 * num2

print(f"{name} you gave numbers {num1} and {num2}")
print(f"Multiplying first and second number will result in product {product:.2f}")

print("Program ending.")
