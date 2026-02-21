import sys


def ft_inventory_system() -> None:

    if len(sys.argv) < 2:
        print("Usage: python3 ft_inventory_system.py sword:1 potion:5 ...")
        return

    valid_items = ["sword", "potion", "shield", "armor", "helmet"]

    inventory = {}
    for arg in sys.argv[1:]:
        try:
            key, value = arg.split(':')
            if not key:
                print(f"Error: invalid format '{arg}', expected name:quantity")
                return
            if key not in valid_items:
                print(f"Error: '{key}' is not a valid item")
                return
            quantity = int(value)
            if quantity < 0:
                print("Error: quantity cannot be negative")
                return
            inventory.update({key: {"quantity": quantity}})
        except ValueError:
            print(f"Error: invalid format '{arg}', expected name:quantity")
            return

    if not inventory:
        print("Error: no valid items parsed")
        return
    
    print("=== Inventory System Analysis ===")
    total_items = 0
    for item in inventory:
        total_items += inventory[item]["quantity"]
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory)}")

    print("\n=== Current Inventory ===")
    for item, value in inventory.items():
        percentage = value["quantity"] / total_items * 100
        print(f"{item}: {value['quantity']} units ({percentage:.1f}%)")

    print("\n=== Inventory Statistics ===")
    largest = None
    smallest = None
    for value in inventory.values():
        q = value["quantity"]
        if largest is None or q > largest:
            largest = q
        if smallest is None or q < smallest:
            smallest = q

    for item in inventory:
        if inventory[item]["quantity"] == largest:
            print(f"Most abundant: {item} ({largest} units)")
            break

    for item in inventory:
        if inventory[item]["quantity"] == smallest:
            print(f"Least abundant: {item} ({smallest} unit)")
            break

    print("\n=== Item Categories ===")
    moderate = {}
    scarce = {}
    for key, value in inventory.items():
        if key == "potion":
            moderate[key] = value["quantity"]
        if key == "sword" or key == "shield" or key == "armor" or key == "helmet":
            scarce[key] = value["quantity"]

    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")

    print("\n=== Management Suggestions ===")
    restock = []
    for key, value in inventory.items():
        if value["quantity"] < 2:
            restock.append(key)
    print(f"Restock needed: {restock}")

    print("\n=== Dictionary Properties Demo ===")
    inventory_keys = []
    inventory_values = []
    for key, value in inventory.items():
        inventory_keys.append(key)
        inventory_values.append(value["quantity"])
    print(f"Dictionary keys: {inventory_keys}")
    print(f"Dictionary values: {inventory_values}")
    if "sword" in inventory:
        print(f"Sample lookup - 'sword':{inventory.get('sword')} in inventory: True")


if __name__ == "__main__":
    try:
        ft_inventory_system()
    except ZeroDivisionError as e:
        print(f"Error: {e}")