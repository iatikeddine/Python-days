from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main() -> None:
    print("\n=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")
    card_deck = Deck()
    fire_dragon = CreatureCard("Fire Dragon", 5,
                               Rarity.LEGENDARY.value, 7, 5)
    lightning_bolt = SpellCard("Lightning Bolt", 3, Rarity.RARE.value,
                               "damage")
    mana_crystal = ArtifactCard("Mana Crystal", 2, Rarity.COMMON.value, 1,
                                "Permanent: +1 mana per turn")

    card_deck.add_card(fire_dragon)
    card_deck.add_card(lightning_bolt)
    card_deck.add_card(mana_crystal)
    print(f"Deck stats: {card_deck.get_deck_stats()}")

    print("\nDrawing and playing cards:\n")
    try:
        card_deck.shuffle()
        for x in range(card_deck.total_cards()):
            chosen_card = card_deck.draw_card()
            print(f"Drew: {chosen_card.name} ({chosen_card.type})")
            print(f"Play result: {chosen_card.play({})}\n")
        print("Polymorphism in action: Same interface, different "
              "card behaviors!")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
