from typing import Dict
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self) -> None:
        self.factory = None
        self.strategy = None
        self.total_turns = 0

    def configure_engine(self,
                         factory: CardFactory, strategy: GameStrategy) -> None:
        if not isinstance(factory, CardFactory):
            raise ValueError("error: factory is not valid")
        if not isinstance(strategy, GameStrategy):
            raise ValueError("error: strategy is not valid")
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> Dict:
        if not self.factory or not self.strategy:
            raise ValueError("error: game engine must be configured first")

        themed_deck = self.factory.create_themed_deck(10)
        hand = themed_deck["cards"]
        battlefield = []

        actions = self.strategy.execute_turn(hand, battlefield)
        self.total_turns += 1

        return {
            "turns_simulated": self.total_turns,
            "strategy_used": self.strategy.get_strategy_name(),
            "actions": actions
        }

    def get_engine_status(self) -> Dict:
        ready_to_play = self.factory is not None and self.strategy is not None

        return {
            "turns_simulated": self.total_turns,
            "strategy": (self.strategy.__class__.__name__
                         if self.strategy else "None"),
            "is_configured": ready_to_play,
            "factory": (self.factory.__class__.__name__
                        if self.factory else "None")
        }
