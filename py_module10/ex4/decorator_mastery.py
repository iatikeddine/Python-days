from typing import Callable, Any
import functools
import time


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return wrapper


@spell_timer
def fireball() -> str:
    time.sleep(0.1)
    return "Result: Fireball cast!"


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            power = None
            if "power" in kwargs:
                power = kwargs["power"]
            else:
                for arg in args:
                    if isinstance(arg, int):
                        power = arg
                        break
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


@power_validator(50)
def spell_power(power: int) -> str:
    return f"Spell power: {power}"


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception:
                    if attempt < max_attempts:
                        print(f"Spell failed, retrying... "
                              f"(attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


@retry_spell(3)
def good_spell() -> str:
    return "Spell works"


@retry_spell(3)
def failure_spell() -> None:
    raise ValueError("never works")


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if not isinstance(name, str) or len(name) < 3:
            return False
        return all(char.isalpha() or char.isspace() for char in name)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    try:
        print("\nTesting spell timer")
        result = fireball()
        print(result)
    except Exception as e:
        print(e)
    try:
        print("\nTesting power validator")
        print(spell_power(50))
        print(spell_power(20))
    except Exception as e:
        print(e)
    try:
        print("\nTesting retry spell")
        print(good_spell())
        print(failure_spell())
    except Exception as e:
        print(e)
    try:
        print("\nTesting MageGuild...")
        guild = MageGuild()
        print(MageGuild.validate_mage_name("Gandalf The White"))
        print(MageGuild.validate_mage_name("X_123"))
        print(guild.cast_spell("Lightning", 15))
        print(guild.cast_spell("Spark", 5))
    except Exception as e:
        print(e)
