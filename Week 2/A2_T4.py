print("Program starting.")
print("Estimate how many minutes you spent on programming...")

t1 = int(input("A1_T1: "))
t2 = int(input("A1_T2: "))
t3 = int(input("A1_T3: "))
t4 = int(input("A1_T4: "))
t5 = int(input("A1_T5: "))
t6 = int(input("A1_T6: "))
t7 = int(input("A1_T7: "))

total = t1 + t2 + t3 + t4 + t5 + t6 + t7
average = total / 7

print()
print(f"In total you spent {total} minutes on programming.")
print(f"Average per task was {average:.2f} min and same rounded to the nearest integer {int(round(average))} min.")

print()
print("Program ending.")
