from typing import Dict, List
from ex3.GameStrategy import GameStrategy
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard


class AggressiveStrategy(GameStrategy):
    def return_cost(self, card: Card) -> int:
        if not isinstance(card, Card):
            raise ValueError("error: unsuported card")
        return card.cost

    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        if not isinstance(hand, list):
            raise ValueError("error: hand is not valid")
        if not isinstance(battlefield, list):
            raise ValueError("error: battlefield is not valid")

        mana_pool = 10
        cards_played = []
        mana_used = 0
        damage_dealt = 0
        sorted_hand = sorted(hand, key=self.return_cost)
        for card in sorted_hand:
            if card.cost <= mana_pool:
                cards_played.append(card.name)
                battlefield.append(card)
                if isinstance(card, CreatureCard):
                    damage_dealt += card.attack
                mana_used += card.cost
                mana_pool -= card.cost
        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": ["Enemy Player"],
            "damage_dealt": damage_dealt
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: List) -> List:
        if not isinstance(available_targets, list) or not available_targets:
            raise ValueError("error: available targets is not valid")
        return available_targets
