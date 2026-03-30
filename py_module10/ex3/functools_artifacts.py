from functools import partial, reduce, lru_cache, singledispatch
import operator
from typing import Callable, Any


def spell_reducer(spells: list[int], operation: str) -> int:
    supported_operations = ["add", "multiply", "max", "min"]
    if operation not in supported_operations:
        raise ValueError("error: invalid operation")

    if operation == "add":
        result = reduce(operator.add, spells)
    elif operation == "multiply":
        result = reduce(operator.mul, spells)
    elif operation == "max":
        result = reduce(max, spells)
    elif operation == "min":
        result = reduce(min, spells)
    return result


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    if not callable(base_enchantment):
        raise ValueError("error: base enchantment is not callable")
    fire_enchant = partial(base_enchantment, 50, "fire")
    ice_enchant = partial(base_enchantment, 50, "ice")
    lightning_enchant = partial(base_enchantment, 50, "lightning")
    return {
        "fire_enchant": fire_enchant,
        "ice_enchant": ice_enchant,
        "lightning_enchant": lightning_enchant
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    @singledispatch
    def cast_spell(magic_input: Any):
        return "Unknown magic type!"

    @cast_spell.register
    def _(damage: int) -> str:
        return f"Casting a damage spell with {damage} power!"

    @cast_spell.register
    def _(enchantment: str) -> str:
        return f"Applying {enchantment} enchantment!"

    @cast_spell.register
    def _(targets: list) -> str:
        return f"Multi-casting to {len(targets)} targets!"

    return cast_spell


if __name__ == "__main__":
    print("\nTesting spell reducer...")
    try:
        spells = [30, 40, 30]
        addition = spell_reducer(spells, "add")
        print(f"Sum: {addition}")
        multi = spell_reducer(spells, "multiply")
        print(f"Product: {multi}")
        maximum = spell_reducer(spells, "max")
        print(f"Max: {maximum}")
        minimum = maximum = spell_reducer(spells, "min")
        print(f"Min: {minimum}")
    except Exception as e:
        print(e)
    try:
        print("\nTesting partial enchanter...")

        def base_enchantement(power: int, element: str, target: str) -> str:
            return f"{target} enchated by {power} {element}"

        enchants = partial_enchanter(base_enchantement)
        print(enchants["fire_enchant"]("Sword"))
        print(enchants["ice_enchant"]("Sheild"))
    except Exception as e:
        print(e)
    try:
        print("\nTesting memoized fibonacci...")
        print(f"fib(10): {memoized_fibonacci(10)}")
        print(f"Fib(15): {memoized_fibonacci(15)}")
    except Exception as e:
        print(e)
    try:
        print("\nTesting spell dispatcher...")
        cast_spell = spell_dispatcher()
        print(cast_spell(7))
    except Exception as e:
        print(e)
