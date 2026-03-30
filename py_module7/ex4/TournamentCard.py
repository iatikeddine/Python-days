from typing import Dict
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, id: str, cost: int, rarity: str, attack: int,
                 health: int) -> None:
        super().__init__(name, cost, rarity)

        if not isinstance(id, str) or not id.strip():
            raise ValueError("error: id is not valid")
        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("error: attack attribute is invalid")
        if not isinstance(health, int) or health < 0:
            raise ValueError("error: health attribute is not valid")

        self.id = id
        self.attack_dmg = attack
        self.health = health
        self.original_health = health
        self.wins = 0
        self.losses = 0
        self.rating = 1000

    def play(self, game_state: Dict) -> Dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost
        }

    def attack(self, target: Card) -> Dict:
        if not isinstance(target, Card):
            raise ValueError("error: invalid card")

        return {
            "attacker": self.name,
            "target": target.name,
            "damage": self.attack_dmg,
        }

    def defend(self, incoming_damage: int) -> Dict:
        if not isinstance(incoming_damage, int) or incoming_damage < 0:
            raise ValueError("error: incoming damage is not valid")
        if self.health >= incoming_damage:
            self.health -= incoming_damage if incoming_damage > 0 else 0
        else:
            self.health = 0

        return {
            "defender": self.name,
            "damage_taken": incoming_damage if incoming_damage > 0 else 0,
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> Dict:
        return {
            "attack": self.attack_dmg,
            "health": self.health
        }

    def update_wins(self, wins: int) -> None:
        if not isinstance(wins, int):
            raise ValueError("error: wins is not valid")
        self.wins += wins if wins > 0 else 0

    def update_losses(self, losses: int) -> None:
        if not isinstance(losses, int):
            raise ValueError("error: losses is not valid")
        self.losses += losses if losses > 0 else 0

    def calculate_rating(self) -> int:
        self.rating = 1000 + (self.wins * 20) - (self.losses * 20)
        return self.rating

    def get_rank_info(self) -> Dict:
        return {
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses
        }

    def get_tournament_stats(self) -> Dict:
        return {
            "name": self.name,
            "id": self.id,
            "rating": self.calculate_rating(),
            "records": f"wins: {self.wins}-losses: {self.losses}"
        }

    def reset_health(self) -> None:
        self.health = self.original_health
