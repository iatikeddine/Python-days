import sys
import math


class ParsingError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


def coordinate_system():
    print("=== Game Coordinate System ===")
    print()

    position_0 = (0, 0, 0)
    x1 = position_0[0]
    y1 = position_0[1]
    z1 = position_0[2]

    position_1 = (10, 20, 5)
    x2 = position_1[0]
    y2 = position_1[1]
    z2 = position_1[2]
    print(f"Position created: {position_1}")

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    print(f"Distance between {position_0} and {position_1}: {distance:.2f}\n")

    if (len(sys.argv) == 2):
        coordinates = sys.argv[1]
        coordinates = coordinates.split(',')
        if len(coordinates) != 3:
            raise ParsingError("Error: Coordinates shoulb be x,y,x")
        else:
            print(f"Parsing coordinates: ")