import sys
import math

print("=== Game Coordinate System ===\n")
positions = [(0, 0, 0),(10, 20, 5)]
distance1 = float(math.sqrt(
    (positions[1][0]-positions[0][0])**2 +
    (positions[1][1]-positions[0][1])**2 +
    (positions[1][2]-positions[0][2])**2)
)
print(f"Position created: {positions[1]}")
print(f"Distance between {positions[0]} and {positions[1]}: {distance1:.2f}")
print()