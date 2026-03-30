from typing import Dict
from ex0.Card import Card


class CreatureCard(Card):
    def __init__(
        self, name: str, cost: int,
            rarity: str, attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)

        if not isinstance(attack, int):
            raise ValueError("error: attack must be a number")
        if not isinstance(health, int):
            raise ValueError("error: health must be a number")
        if attack <= 0 or health <= 0:
            raise ValueError("error: health and attack should be positive")

        self.type = "Creature"
        self.attack = attack
        self.health = health

    def play(self, game_state: Dict) -> Dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }

    def attack_target(self, target: "CreatureCard") -> Dict:
        if not isinstance(target, CreatureCard):
            raise ValueError("error: target must be a valid card")
        if target.health >= self.attack:
            target.health -= self.attack
        else:
            target.health = 0
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": True
        }
