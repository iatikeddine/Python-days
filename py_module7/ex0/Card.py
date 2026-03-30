from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict


class Rarity(Enum):
    COMMON = "Common"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        if not isinstance(name, str):
            raise ValueError("error: name must be a string")
        if not name.strip():
            raise ValueError("error: name cannot be empty")
        if not isinstance(cost, int):
            raise ValueError("error: cost must be a number")
        if not isinstance(rarity, str):
            raise ValueError("error: rarity must be a string")
        if cost <= 0:
            raise ValueError("error: cost must be positive")
        self.name = name
        self.cost = cost
        self.rarity = rarity

    def play(self, game_state: Dict) -> Dict:
        pass
    play = abstractmethod(play)

    def get_card_info(self) -> Dict:
        return self.__dict__

    def is_playable(self, available_mana: int) -> bool:
        if not isinstance(available_mana, int):
            raise ValueError("error: availabe mana should be a number")
        if available_mana >= self.cost:
            return True
        return False
