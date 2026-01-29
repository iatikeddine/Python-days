import sys

inventory = {
    "sword": 1
}

if len(sys.argv) < 2:
    print("")

print("=== Inventory System Analysis ===")
total_items = 0
for item in inventory:
    total_items += inventory[item]
print(f"Total items in inventory: {total_items}")
print(f"Unique item types: {len(inventory)}")

print()
print("=== Current Inventory ===")
percentage = 0
for item in inventory:
    percentage = inventory[item] / total_items * 100
    print(f"{item}: {inventory[item]} units ({percentage:.1f}%)")

print()
print("=== Inventory Statistics ===")
largest = None
smallest = None
for value in inventory.values():
    if largest is None or value > largest:
        largest = value
    if smallest is None or value < smallest:
        smallest = value


for item in inventory:
    if inventory[item] == largest:
        print(f"Most abundant: {item} ({largest} units)")

for item in inventory:
    if inventory[item] == smallest:
        print(f"Least abundant: {item} ({smallest} unit)")
        break

print()
print("=== Item Categories ===")
moderate = {}
scarce = {}
for key, value in inventory.items():
    if key == "potions":
        moderate[key] = value
    if key == "sword" or key == "shield" or key == "armor" or key == "helmet":
        scarce[key] = value

print(f"Moderate: {moderate}")
print(f"Scarce: {scarce}")

print()
print("=== Management Suggestions ===")
restock = []
for key, value in inventory.items():
    if value < 2:
        restock.append(key)
print(f"Restock needed: {restock}")

print()
print("=== Dictionary Properties Demo ===")
inventory_keys = []
inventory_values = []
for key, value in inventory.items():
    inventory_keys.append(key)
    inventory_values.append(value)
print(f"Dictionary keys: {inventory_keys}")
print(f"Dictionary values: {inventory_values}")
if "sword" in inventory:
    print("Sample lookup - 'sword' in inventory: True")