from typing import Dict
from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        if not isinstance(durability, int):
            raise ValueError("error: durability must be a number")
        if durability <= 0:
            raise ValueError("error: negative durability")
        if not isinstance(effect, str) or not effect.strip():
            raise ValueError("error: effect is not valid")
        self.durability = durability
        self.effect = effect
        self.type = "artifact"

    def play(self, game_state: Dict) -> Dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect
        }

    def activate_ability(self) -> Dict:
        return {
            "card_activated": self.name,
            "effect": self.effect
        }
