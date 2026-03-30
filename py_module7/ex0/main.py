from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity


def main() -> None:
    print("\n=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    fire_dragon = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY.value, 7, 5)
    goblin_warrior = CreatureCard(
        "Goblin Warrior", 2, Rarity.COMMON.value, 3, 2)
    print("CreatureCard Info:")
    print(fire_dragon.get_card_info())

    print("\nPlaying Fire Dragon with 6 mana available:")
    try:
        mana_available = 6
        print(f"Playable: {fire_dragon.is_playable(mana_available)}")
        print(f"Play result: {fire_dragon.play({})}")
    except Exception as e:
        print(e)

    print("\nFire Dragon attacks Goblin Warrior:")
    try:
        print(f"Attack result: {fire_dragon.attack_target(goblin_warrior)}")
    except Exception as e:
        print(e)

    insufficient_mana = 3
    print(f"\nTesting insufficient mana ({insufficient_mana} available):")
    print(f"Playable: {fire_dragon.is_playable(insufficient_mana)}")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
