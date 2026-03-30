from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main() -> None:
    print("\n=== DataDeck Game Engine ===\n")
    print("Configuring Fantasy Card Game...")
    try:
        factory = FantasyCardFactory()
        strategy = AggressiveStrategy()
        print(f"Factory: {factory.__class__.__name__}")
        print(f"strategy: {strategy.get_strategy_name()}")
        print(f"available types: {factory.get_supported_types()}\n")
    except Exception as e:
        print(e)

    print("Simulating aggressive turn...")
    try:
        engine = GameEngine()
        engine.configure_engine(factory, strategy)
        simulation = engine.simulate_turn()
        print(f"Hand: {simulation['actions']['cards_played']}")

        print("\nTurn execution:")
        print(f"Strategy: {strategy.get_strategy_name()}")
        print(f"actions: {simulation['actions']}")

        print("\nGame Reports:")
        print(f"{engine.get_engine_status()}")
        print("\nAbstract Factory + Strategy Pattern: Maximum "
              "flexibility achieved!")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
