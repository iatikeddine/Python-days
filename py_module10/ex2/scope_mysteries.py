from typing import Callable, Any


def mage_counter() -> Callable:
    count = 0

    def calls_count() -> int:
        nonlocal count
        count += 1
        return count
    return calls_count


def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power

    def accumulate_power(added_power: int) -> int:
        nonlocal total_power
        total_power += added_power
        return total_power
    return accumulate_power


def enchantment_factory(enchantment_type: str) -> Callable:

    def enchantement_name(name: str) -> str:
        return f"{enchantment_type} {name}"
    return enchantement_name


def memory_vault() -> dict[str, Callable]:
    vault = {}

    def store(key: str, value: Any) -> None:
        vault[key] = value

    def recall(key: str) -> Any:
        if key in vault:
            return vault[key]
        return "Memory not found"

    return {
        "store": store,
        "recall": recall
    }


if __name__ == "__main__":
    print("Testing mage counter...")
    try:
        counter = mage_counter()
        for x in range(1, 4):
            print(f"Call {x}: {counter()}")
    except Exception as e:
        print(e)
    try:
        print("\nTesting spell acumulator...")
        acumulate = spell_accumulator(20)
        for x in range(1, 3):
            print(f"total power {x}: {acumulate(10)}")
        acumulate = spell_accumulator(100)
        for x in range(2, 4):
            print(f"total power {x}: {acumulate(10)}")
    except Exception as e:
        print(e)
    try:
        print("\nTesting enchantment factory...")
        enchantement = enchantment_factory("Flaming")
        print(enchantement("Sword"))
        enchantement = enchantment_factory("Frozen")
        print(enchantement("Shield"))
    except Exception as e:
        print(e)
    try:
        print("\nTesting memory vault...")
        memory = memory_vault()
        memory["store"]("message", "Message retreived successfully")
        message = memory["recall"]("message")
        print(message)
    except Exception as e:
        print(e)
