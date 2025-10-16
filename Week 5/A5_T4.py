def askDimension(pPrompt: str) -> float:
    feed = float(input(f"Insert {pPrompt}: "))
    return feed


def calcRectangleArea(pWidth: float, pHeight: float) -> float:
    area = pWidth * pHeight
    return area


def main():
    print("Program starting.")
    width = askDimension("width")
    height = askDimension("height")
    print()
    area = calcRectangleArea(width, height)
    print(f"Area is {area:.1f}.")
    print("Program ending.")
    return None


main()
