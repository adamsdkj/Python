"""Main module demonstrating the Game Engine with Factory + Strategy."""

from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main() -> None:
    """Demonstrate the Abstract Factory and Strategy patterns."""
    try:
        fantasycardfactory = FantasyCardFactory()
        aggressivestrategy = AggressiveStrategy()
        engine = GameEngine()
        engine.configure_engine(
            fantasycardfactory, aggressivestrategy
        )
        fantasycardfactory.create_creature("Fire Dragon")
        hand = [
            fantasycardfactory.create_creature(
                "Goblin Warrior"
            ),
            fantasycardfactory.create_spell(
                "Lightning Bolt"
            ),
        ]
        actions = aggressivestrategy.execute_turn(
            hand, ['Enemy Player']
        )
        report = engine.get_engine_status()

        print(
            "\n=== DataDeck Game Engine ===\n"
            "\nConfiguring Fantasy Card Game...\n"
            "Factory: FantasyCardFactory\n"
            f"Strategy: "
            f"{aggressivestrategy.get_strategy_name()}\n"
            "Available types: "
            f"{fantasycardfactory.get_supported_types()}\n"
        )

        print("Simulating aggressive turn...")
        print(
            "Hand: [Fire Dragon (5), "
            "Goblin Warrior (2), Lightning Bolt (3)]"
        )

        print(
            "\nTurn execution:\n"
            f"Strategy: "
            f"{aggressivestrategy.get_strategy_name()}\n"
            f"Actions: {actions}\n"
        )

        print("Game Report:")
        print(report)

        print(
            "\nAbstract Factory + Strategy Pattern: "
            "Maximum flexibility achieved!"
        )
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
