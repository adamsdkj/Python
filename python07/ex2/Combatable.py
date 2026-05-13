"""Combatable module defining the combat interface."""

from abc import ABC, abstractmethod
from typing import Dict


class Combatable(ABC):
    """Abstract interface for cards that can engage in combat."""

    @abstractmethod
    def attack(self, target: str) -> Dict:
        """Attack a target.

        Args:
            target: The name of the target.

        Returns:
            A dict describing the attack result.
        """
        ...

    @abstractmethod
    def defend(self, incoming_damage: int) -> Dict:
        """Defend against incoming damage.

        Args:
            incoming_damage: The amount of damage to defend.

        Returns:
            A dict describing the defense result.
        """
        ...

    @abstractmethod
    def get_combat_stats(self) -> Dict:
        """Return combat statistics.

        Returns:
            A dict with combat-related stats.
        """
        ...
