"""GameStrategy module defining the strategy interface."""

from abc import ABC, abstractmethod
from typing import List, Dict


class GameStrategy(ABC):
    """Abstract interface for game strategies."""

    @abstractmethod
    def execute_turn(
        self, hand: List, battlefield: list
    ) -> Dict:
        """Execute a turn with the given hand and battlefield.

        Args:
            hand: List of cards in hand.
            battlefield: List of entities on the battlefield.

        Returns:
            A dict describing the turn actions.
        """
        ...

    @abstractmethod
    def get_strategy_name(self) -> str:
        """Return the name of this strategy.

        Returns:
            The strategy name.
        """
        ...

    @abstractmethod
    def prioritize_targets(
        self, available_targets: List
    ) -> List:
        """Prioritize available targets.

        Args:
            available_targets: List of potential targets.

        Returns:
            Sorted list of targets by priority.
        """
        ...
