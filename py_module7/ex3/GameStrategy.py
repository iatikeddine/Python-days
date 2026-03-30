from typing import Dict, List
from abc import ABC, abstractmethod


class GameStrategy(ABC):
    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        pass
    execute_turn = abstractmethod(execute_turn)

    def get_strategy_name(self) -> str:
        pass
    get_strategy_name = abstractmethod(get_strategy_name)

    def prioritize_targets(self, available_targets: List) -> List:
        pass
    prioritize_targets = abstractmethod(prioritize_targets)
