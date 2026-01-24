
print()
print("=== Import Transmutation Mastery ===")
print()

print("Method 1 - Full module import:")
from alchemy.elements import create_fire
print(f"alchemy.elements.create_fire(): {create_fire()}")

print()
print("Method 2 - Specific function import:")
import alchemy.elements
print(f"create_water(): {alchemy.elements.create_water()}")

print()
print("Method 3 - Aliased import:")
from alchemy.potions import healing_potion as heal
print(f"heal(): {heal()}")

print()
print("Method 4 - Multiple imports:")
from alchemy.elements import create_earth, create_fire
from alchemy.potions import strength_potion
print(f"create_earth(): {create_earth()}")
print(f"create_fire(): {create_fire()}")
print(f"strength_potion(): {strength_potion()}")

print()
print("All import transmutation methods mastered!")