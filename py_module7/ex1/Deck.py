from typing import Dict
from ex0.Card import Card
import random


class Deck:
    def __init__(self) -> None:
        self.cards = []

    def add_card(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise ValueError("error: not a valid card")
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        if not isinstance(card_name, str):
            raise ValueError("error: name is not valid")
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            raise ValueError("error: you can't draw a card from empty deck")
        card = self.cards.pop()
        return card

    def total_cards(self) -> int:
        if self.cards:
            return len(self.cards)
        return 0

    def get_deck_stats(self) -> Dict:
        return {
            "total_cards": len(self.cards),
            "creatures": len([card for card in self.cards
                             if card.type == "creature"]),
            "spells": len([card for card in self.cards
                          if card.type == "spell"]),
            "artifacts": len([card for card in self.cards
                             if card.type == "artifact"]),
            "avg_cost": (
                round(sum([card.cost for card in self.cards])
                      / len(self.cards), 1)
                if self.cards else 0)
        }
