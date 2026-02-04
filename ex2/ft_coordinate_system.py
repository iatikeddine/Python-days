import sys
import math

def coordinate_system() -> None:
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

    if len(sys.argv) == 2:
        coordinates = sys.argv[1]
        coordinates = coordinates.split(',')
        if len(coordinates) != 3:
            print("Error: Coordinates shoulb be x,y,x")
            return
        try:
            coordinates = [float(cord) for cord in coordinates]
        except ValueError as e:
            print(f"Error parsing coordinates: {e}")
            print(f'Error details - Type: ValueError, Args: ("{e}")')
        else:
            print(f'Parsing coordinates: '
                  f'"{coordinates[0]},{coordinates[1]},{coordinates[2]}"')
            position_1 = (tuple(coordinates))
            print(f"Parsed position: {position_1}")
            x2 = position_1[0]
            y2 = position_1[1]
            z2 = position_1[2]
            distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
            print(f"Distance between {position_0} and {position_1}: {distance:.1f}")
    elif len(sys.argv) > 2:
        print("Only 1 set of cordinates allowed in this format [x,y,z]")

    print("\nUnpacking demonstration:")
    x, y, z = position_1
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")

if __name__ == "__main__":
    coordinate_system()