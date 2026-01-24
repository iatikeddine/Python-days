import alchemy
from alchemy.elements import create_fire
from alchemy.elements import create_water
from alchemy.elements import create_earth
from alchemy.elements import create_air

print()
print("=== Sacred Scroll Mastery ===")
print()

print("Testing direct module access:")
print(f"alchemy.elements.create_fire(): {create_fire()}")
print(f"alchemy.elements.create_water(): {create_water()}")
print(f"alchemy.elements.create_earth(): {create_earth()}")
print(f"alchemy.elements.create_air(): {create_air()}")

print()
print("Testing package-level access (controlled by __init__.py):")
print(f"alchemy.create_fire(): {alchemy.create_fire()}")
print(f"alchemy.create_water(): {alchemy.create_water()}")
try:
    alchemy.create_earth()
except AttributeError:
    print(f"alchemy.create_earth(): AttributeError - not exposed")

try:
    alchemy.create_air()
except AttributeError:
    print(f"alchemy.create_air(): AttributeError - not exposed")

print()
print("Package metadata:")
print(f"Version: {alchemy.__version__}")
print(f"Author: {alchemy.__author__}")