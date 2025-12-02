import sys
import os

print("Program starting.")

filename = input("Insert filename: ")

if not os.path.isfile(filename):
    print("Error! File '{}' does not exist.".format(filename))
    sys.exit(1)


print("## {} ##".format(filename))

with open(filename, "r") as f:
    for line in f:
        print(line.rstrip())

print("## {} ##".format(filename))

print("Program ending.")
