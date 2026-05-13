"""Rankable module defining the ranking interface."""

from abc import ABC, abstractmethod
from typing import Dict


class Rankable(ABC):
    """Abstract interface for cards that can be ranked."""

    @abstractmethod
    def calculate_rating(self) -> int:
        """Calculate and return the card's rating.

        Returns:
            The calculated rating value.
        """
        ...

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """Update the number of wins.

        Args:
            wins: Number of wins to add.
        """
        ...

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """Update the number of losses.

        Args:
            losses: Number of losses to add.
        """
        ...

    @abstractmethod
    def get_rank_info(self) -> Dict:
        """Return ranking information.

        Returns:
            A dict with ranking details.
        """
        ...
