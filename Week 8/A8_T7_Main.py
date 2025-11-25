from svgwrite import Drawing
from drawLib import drawSquare, drawCircle, drawHexagon, saveSvg


def showMenu() -> None:
    print("Options:")
    print("1 - Draw square")
    print("2 - Draw circle")
    print("3 - Draw hexagon")
    print("4 - Save svg")
    print("0 - Exit")


def main() -> None:
    print("Program starting.")

    dwg = Drawing()  # filename will be given when saving

    while True:
        showMenu()
        choice = input("Your choice: ")

        if choice == "1":
            print("Insert square")
            left = float(input("- Left edge position: "))
            top = float(input("- Top edge position: "))
            side = float(input("- Side length: "))
            fill = input("- Fill color: ")
            stroke = input("- Stroke color: ")
            drawSquare(dwg, left=left, top=top, sideLength=side,
                       color=fill, strokeColor=stroke)
            print()

        elif choice == "2":
            print("Insert circle")
            cx = float(input("- Center X position: "))
            cy = float(input("- Center Y position: "))
            r = float(input("- Radius: "))
            fill = input("- Fill color: ")
            stroke = input("- Stroke color: ")
            drawCircle(dwg, centerX=cx, centerY=cy, radius=r,
                       color=fill, stroke=stroke)
            print()

        elif choice == "3":
            print("Insert hexagon details:")
            cx = float(input("Middle point X: "))
            cy = float(input("Middle point Y: "))
            apothem = float(input("Apothem length: "))
            fill = input("Insert fill: ")
            stroke = input("Insert stroke: ")
            drawHexagon(dwg, centerX=cx, centerY=cy, apothem=apothem,
                        color=fill, stroke=stroke)
            print()

        elif choice == "4":
            filename = input("Insert filename: ")
            print(f'Saving file to "{filename}"')
            proceed = input("Proceed (y/n)?: ")
            if proceed.lower() == "y":
                saveSvg(dwg, filename)
                print("Vector saved successfully!")
            else:
                print("Save cancelled.")
            print()

        elif choice == "0":
            print("Exiting program.")
            print()
            break

        else:
            print("Invalid choice.")
            print()

    print("Program ending.")


if __name__ == "__main__":
    main()
