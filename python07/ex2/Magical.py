"""Magical module defining the magic interface."""

from abc import ABC, abstractmethod
from typing import Dict, List


class Magical(ABC):
    """Abstract interface for cards that can use magic."""

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: List) -> Dict:
        """Cast a spell on targets.

        Args:
            spell_name: The name of the spell to cast.
            targets: List of targets for the spell.

        Returns:
            A dict describing the spell result.
        """
        ...

    @abstractmethod
    def channel_mana(self, amount: int) -> Dict:
        """Channel mana energy.

        Args:
            amount: The amount of mana to channel.

        Returns:
            A dict describing the channeling result.
        """
        ...

    @abstractmethod
    def get_magic_stats(self) -> Dict:
        """Return magic-related statistics.

        Returns:
            A dict with magic-related stats.
        """
        ...
