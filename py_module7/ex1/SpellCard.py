from typing import Dict, List
from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)

        if not isinstance(effect_type, str) or not effect_type.strip():
            raise ValueError("error: effect type is not valid")

        self.available_effects = ["damage", "heal", "buff", "debuff"]
        self.effect_type = (
            effect_type
            if effect_type in self.available_effects
            else "damage")
        self.type = "spell"

    def play(self, game_state: Dict) -> Dict:
        if self.effect_type.lower() == "damage":
            resolved_effect = "Deal 3 damage to target"
        elif self.effect_type.lower() == "heal":
            resolved_effect = "Added 3 Hp to creature"
        elif self.effect_type.lower() == "buff":
            resolved_effect = "Grant creature +2 attack power"
        elif self.effect_type == "debuff":
            resolved_effect = "Remove creature abilities for next turn"

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": resolved_effect
        }

    def resolve_effect(self, targets: List) -> Dict:
        if not isinstance(targets, list):
            raise ValueError("error: targets is not a list")
        for target in targets:
            if not isinstance(target, Card):
                raise ValueError("error: list contains a non valid card")
        return {
            "caster": self.name,
            "targets": [target.name
                        for target in targets] if targets else None,
            "effect_type": self.effect_type
        }
