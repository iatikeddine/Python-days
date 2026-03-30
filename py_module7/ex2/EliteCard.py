from typing import Dict, List
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int, mana_pool: int, armor: int) -> None:
        super().__init__(name, cost, rarity)

        if not isinstance(attack, int):
            raise ValueError("error: attack must be a number")
        if not isinstance(health, int):
            raise ValueError("error: health must be a number")
        if attack <= 0 or health <= 0:
            raise ValueError("error: attack and health must be positive")
        if not isinstance(mana_pool, int):
            raise ValueError("error: mana pool should be a number")
        if mana_pool <= 0:
            raise ValueError("error: mana pool is negative")
        if not isinstance(armor, int):
            raise ValueError("error: armor should be a number")
        if armor <= 0:
            raise ValueError("error: armor is negative")

        self.health = health
        self.ongoing_damage = attack
        self.mana_pool = mana_pool
        self.armor = armor

    def play(self, game_state: Dict) -> Dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite Card deployed"
        }

    def attack(self, target: str) -> Dict:
        if not isinstance(target, str) or not target.strip():
            raise ValueError("error: invalid data for attack action")

        return {
            "attacker": self.name,
            "target": target,
            "damage": self.ongoing_damage,
            "combat_type": "melee"
        }

    def defend(self, incoming_damage: int) -> Dict:
        if not isinstance(incoming_damage, int) or incoming_damage < 0:
            raise ValueError("error: incoming damage is not valid")
        final_damage = max(0, incoming_damage - self.armor)
        damage_blocked = min(incoming_damage, self.armor)
        self.health -= final_damage

        return {
            "defender": self.name,
            "damage_taken": final_damage,
            "damage_blocked": damage_blocked,
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> Dict:
        return {
            "attack": self.ongoing_damage,
            "health": self.health,
            "armor": self.armor
        }

    def cast_spell(self, spell_name: str, targets: List) -> Dict:
        if not isinstance(spell_name, str):
            raise ValueError("error: spell name is not valid")
        if not spell_name.strip():
            raise ValueError("error: spell name is empty")
        if not isinstance(targets, list):
            raise ValueError("error: targets must be a list")

        if self.mana_pool > self.cost * len(targets):
            self.mana_pool -= self.cost * len(targets)
        else:
            self.mana_pool = 0

        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": self.cost * len(targets)
        }

    def channel_mana(self, amount: int) -> Dict:
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("error: mana amount is not valid")
        self.mana_pool += amount
        return {
            "channeled": amount,
            "total_mana": self.mana_pool
        }

    def get_magic_stats(self) -> Dict:
        return {
            "mana_pool": self.mana_pool
        }
