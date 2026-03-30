from ex2.EliteCard import EliteCard
from ex0.Card import Rarity


def main() -> None:
    print("\n=== DataDeck Ability System ===\n")
    classes = EliteCard.__bases__
    for cls in classes:
        methods = [
            name for name, value in cls.__dict__.items()
            if callable(value) and not name.startswith("_")
        ]
        print(f"- {cls.__name__}: {methods}")

    print("\nPlaying Arcane Warrior (Elite Card):\n")
    arcane_warrior = EliteCard("Arcane Warrior", 2,
                               Rarity.LEGENDARY.value, 5, 10, 10, 3)

    print("Combat phase:")
    try:
        print(f"Attack result: {arcane_warrior.attack('Enemy')}")
        print(f"Deffend result: {arcane_warrior.defend(5)}")
    except Exception as e:
        print(e)

    print("\nMagic phase:")
    try:
        targets = ["Enemy1", "Enemy2"]
        print(f"Spell cast: {arcane_warrior.cast_spell('fire_ball', targets)}")
        print(f"Mana channeled: {arcane_warrior.channel_mana(3)}")
    except Exception as e:
        print(e)

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
