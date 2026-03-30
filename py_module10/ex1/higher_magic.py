from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    if not callable(spell1) or not callable(spell2):
        raise ValueError("error: invalid callables")

    def combined(*args, **kwargs) -> tuple:
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return combined


def fireball(creature: str) -> str:
    return f"Fireball hits {creature}"


def heal(creature: str) -> str:
    return f"Heals {creature}"


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    if not callable(base_spell):
        raise ValueError("error: invalid callable")

    def mul(*args, **kwargs) -> int:
        result = base_spell(*args, **kwargs)
        return result * multiplier
    return mul


def base_spell() -> int:
    return 10


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    if not callable(condition) or not callable(spell):
        raise ValueError("error: invalid callables")

    def cast_spell(*args, **kwargs) -> str:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return cast_spell


def condition(target: str) -> bool:
    if target:
        return True
    return False


def spell(target: str) -> str:
    return f"casted spell on {target}"


def spell_sequence(spells: list[Callable]) -> Callable:

    def cast_spells(*args, **kwargs) -> list:
        results = []
        for spell in spells:
            if not callable(spell):
                raise ValueError("error: spell is not callable")
            results.append(spell(*args, **kwargs))
        return results
    return cast_spells


if __name__ == "__main__":
    try:
        print("\nTesting spell combiner...")
        combined_func = spell_combiner(fireball, heal)
        result_1, result_2 = combined_func("Dragon")
        print(f"Combined spell result: {result_1}, {result_2}")
    except Exception as e:
        print(e)
    try:
        print("\nTesting power amplifier...")
        mul = power_amplifier(base_spell, 3)
        print(f"Original: 10, Amplified: {mul()}")
        mul_1 = power_amplifier(base_spell, 5)
        print(f"Original: 10, Amplified: {mul_1()}")
    except Exception as e:
        print(e)
    try:
        print("\nTesting conditional caster")
        cast = conditional_caster(condition, spell)
        print(cast("Dragon"))
    except Exception as e:
        print(e)
