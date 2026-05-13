"""GameEngine module for orchestrating card game simulation."""

from typing import Dict

from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    """Engine that combines a factory and strategy to simulate games."""

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        """Configure the engine with a factory and strategy.

        Args:
            factory: The card factory to use.
            strategy: The game strategy to use.
        """
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> Dict:
        """Simulate a single game turn.

        Returns:
            A dict describing the turn actions.
        """
        cards = self.factory.create_themed_deck(3)
        list_cards = [c for c in cards.values()]
        return self.strategy.execute_turn(
            list_cards, ['Enemy Player']
        )

    def get_engine_status(self) -> Dict:
        """Get the current engine status.

        Returns:
            A dict with turns, strategy, damage, and cards info.
        """
        result: Dict = {
            'turns_simulated': self.strategy.turns_simulated,
            'strategy_used': self.strategy.get_strategy_name(),
            'total_damage': self.strategy.total_damage,
            'cards_created': self.factory.created,
        }
        return result
