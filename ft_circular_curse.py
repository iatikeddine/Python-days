import alchemy.grimoire

print()
print("=== Circular Curse Breaking ===")
print()

print("Testing ingredient validation:")
print(f'validate_ingredients("fire air"): {alchemy.grimoire.validate_ingredients("fire air")}')
print(f'validate_ingredients("dragon scales"): {alchemy.grimoire.validate_ingredients("dragon scales")}')

print()
print("Testing spell recording with validation:")
print(f'record_spell("Fireball", "fire air"): {alchemy.grimoire.record_spell("Fireball", "fire air")}')
print(f'record_spell("Dark Magic", "shadow"): {alchemy.grimoire.record_spell("Dark Magic", "shadow")}')

from alchemy.grimoire import record_spell
print()
print("Testing late import technique:")
print(f'record_spell("Lightning", "air"): {record_spell("Lightning", "air")}')

print()
print("Circular dependency curse avoided using late imports!")
print("All spells processed safely!")