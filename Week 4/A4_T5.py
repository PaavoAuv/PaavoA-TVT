

print("Program.starting.\n")

start = int(input("Insert.starting.point.: "))
stop = int(input("Insert.stopping.point.: "))
inspect = int(input("Insert.inspection.point.: "))

error = False
if start >= stop:
    print("Starting.point.value.must.be.less.than.the.stopping.point.value.")
    error = True

if inspect < start or inspect > stop:
    print("Inspection.value.must.be.within.the.range.of.start.and.stop.")
    error = True

if error:
    print("\nProgram.ending.")
else:
    print("\nFirst.loop...inspection.with.break:")
    for i in range(start, stop + 1):
        if i == inspect:
            break
        print(i, end=" ")
    print()

    print("Second.loop...inspection.with.continue:")
    for i in range(start, stop + 1):
        if i == inspect:
            continue
        print(i, end=" ")
    print("\n\nProgram.ending.")
