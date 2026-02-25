import sys
import math


class InvalidCordsError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


def coordinate_system() -> None:
    print("=== Game Coordinate System ===\n")

    try:
        position_0 = (0, 0, 0)
        x1, y1, z1 = (int(x) for x in position_0)

        position_1 = (10, 20, 5)
        x2, y2, z2 = (int(x) for x in position_1)
    except (ValueError, TypeError):
        raise InvalidCordsError("Error: Position is not valid")
    print(f"Position created: {position_1}")

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    print(f"Distance between {position_0} and {position_1}: {distance:.2f}\n")

    if len(sys.argv) == 2:
        coordinates = sys.argv[1]
        coordinates = coordinates.split(',')
        if len(coordinates) != 3:
            raise InvalidCordsError("Error: Coordinates should be x,y,z")
        try:
            coordinates = [int(cord) for cord in coordinates]
        except ValueError as e:
            error_message = e.args[0]
            print(f"Error parsing coordinates: {error_message}")
            print(f'Error details - Type: ValueError, Args: '
                  f'("{error_message}")')
        else:
            print(f'Parsing coordinates: '
                  f'"{coordinates[0]},{coordinates[1]},{coordinates[2]}"')
            position_1 = tuple(coordinates)
            print(f"Parsed position: {position_1}")
            x2, y2, z2 = position_1
            distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
            print(f"Distance between {position_0} and {position_1}: "
                  f"{distance:.1f}")
    elif len(sys.argv) > 2:
        print("Only 1 set of coordinates allowed in this format [x,y,z]")

    print("\nUnpacking demonstration:")
    x, y, z = position_1
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    try:
        coordinate_system()
    except InvalidCordsError as e:
        message = e.args[0]
        print(message)
