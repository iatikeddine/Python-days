from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform
from ex0.Card import Rarity


def main() -> None:
    print("=== DataDeck Tournament Platform ===\n")
    print("Registering Tournament Cards...")

    try:
        platform = TournamentPlatform()
        dragon = TournamentCard("Fire Dragon", "dragon_001",
                                5, Rarity.LEGENDARY.value, 7, 5)
        wizard = TournamentCard("Ice Wizard", "wizard_001", 4,
                                Rarity.RARE.value, 5, 4)

        platform.register_card(dragon)
        platform.register_card(wizard)

        for card in [dragon, wizard]:
            print(f"{card.name} (ID: {card.id}):")
            print("  Interfaces: [Card, Combatable, Rankable]")
            print(f"  Rating: {card.rating}")
            print(f"  Record: {card.wins}-{card.losses}")

        print("\nCreating tournament match...")
        match_result = platform.create_match(dragon.id, wizard.id)
        print(f"Match result: {match_result}\n")

        print("Tournament Leaderboard:")
        leaderboard = platform.get_leaderboard()
        for index, card in enumerate(leaderboard, start=1):
            print(f"{index}. {card.name} - "
                  f"Rating: {card.rating} ({card.wins}-{card.losses})")

        print("\nPlatform Report:")
        print(platform.generate_tournament_report())

        print("\n=== Tournament Platform Successfully Deployed! ===")
        print("All abstract patterns working together harmoniously!")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
