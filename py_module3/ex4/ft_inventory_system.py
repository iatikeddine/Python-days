import sys


class InvalidFormat(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


def ft_inventory_system() -> None:

    if len(sys.argv) < 2:
        raise InvalidFormat("Usage: python3 ft_inventory_system.py sword:1 "
                            "potion:5 ...")

    valid_items = ["sword", "potion", "shield", "armor", "helmet"]

    inventory = {}
    for arg in sys.argv[1:]:
        try:
            key, value = arg.split(':')
            if not key:
                raise InvalidFormat(f"invalid format '{arg}', "
                                    f"expected name:quantity")
            if key not in valid_items:
                raise InvalidFormat(f"'{key}' is not a valid item")
            quantity = int(value)
            if quantity < 0:
                raise InvalidFormat("quantity cannot be negative")
            inventory.update({key: {"quantity": quantity}})
        except ValueError:
            raise ValueError(f"Error: invalid format '{arg}', expected "
                             f"name:quantity")

    if not inventory:
        raise InvalidFormat("no valid items parsed")

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

    for item in inventory.keys():
        if inventory[item]["quantity"] == smallest:
            print(f"Least abundant: {item} ({smallest} unit)")
            break

    print("\n=== Item Categories ===")
    moderate = {}
    scarce = {}
    for key, value in inventory.items():
        if key == "potion":
            moderate[key] = value["quantity"]
        if key == "sword" or key == "shield" or key == "armor" or \
                key == "helmet":
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
        print(f"Sample lookup - 'sword':{inventory.get('sword')} in "
              f"inventory: True")


if __name__ == "__main__":
    try:
        ft_inventory_system()
    except (InvalidFormat, ZeroDivisionError, ValueError) as e:
        print(f"Error: {e}")
