import math
from svgwrite import Drawing
from svgwrite.shapes import Rect, Circle, Polygon


def drawSquare(
    PDwg: Drawing,
    left: float,
    top: float,
    sideLength: float,
    color: str,
    strokeColor: str
) -> None:
    """
    Draw a square (rect with equal sides) into the given Drawing.
    """
    PDwg.add(
        Rect(
            insert=(left, top),
            size=(sideLength, sideLength),
            fill=color,
            stroke=strokeColor
        )
    )


def drawCircle(
    PDwg: Drawing,
    centerX: float,
    centerY: float,
    radius: float,
    color: str,
    stroke: str
) -> None:
    """
    Draw a circle into the given Drawing.
    """
    PDwg.add(
        Circle(
            center=(centerX, centerY),
            r=radius,
            fill=color,
            stroke=stroke
        )
    )


def drawHexagon(
    PDwg: Drawing,
    centerX: float,
    centerY: float,
    apothem: float,
    color: str,
    stroke: str
) -> None:
    """
    Draw a regular hexagon using center point and apothem (inradius).

    SVG coordinates: origin top-left, x right, y down.
    We:
      1) Compute circumradius R from apothem a:
           a = R * cos(π/6)  =>  R = a / cos(30°)
      2) Take angles (deg): 300, 0, 60, 120, 180, 240
         which correspond to:
           Top Right, Right, Bottom Right,
           Bottom Left, Left, Top Left
      3) Compute points, round to integers, and build Polygon.
    """
    # circumradius
    R = apothem / math.cos(math.radians(30))

    angles_deg = [300, 0, 60, 120, 180, 240]
    points: list[tuple[int, int]] = []

    for angle in angles_deg:
        rad = math.radians(angle)
        # y increases downwards in SVG
        x = centerX + R * math.cos(rad)
        y = centerY + R * math.sin(rad)
        points.append((round(x), round(y)))

    PDwg.add(
        Polygon(
            points=points,
            fill=color,
            stroke=stroke
        )
    )


def saveSvg(PDwg: Drawing, filename: str) -> None:
    """
    Save the Drawing as an SVG file in pretty format with 2-space indent.
    """
    PDwg.saveas(filename, pretty=True, indent=2)
