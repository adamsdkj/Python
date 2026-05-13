"""CardFactory module defining the abstract factory interface."""

from abc import ABC, abstractmethod
from typing import Dict, Optional, Union

from ex0.Card import Card


class CardFactory(ABC):
    """Abstract factory for creating different types of cards."""

    @abstractmethod
    def create_creature(
        self, name_or_power: Optional[Union[str, int]] = None
    ) -> Card:
        """Create a creature card.

        Args:
            name_or_power: Name or power level for the creature.

        Returns:
            A Card instance.
        """
        ...

    @abstractmethod
    def create_spell(
        self, name_or_power: Optional[Union[str, int]] = None
    ) -> Card:
        """Create a spell card.

        Args:
            name_or_power: Name or power level for the spell.

        Returns:
            A Card instance.
        """
        ...

    @abstractmethod
    def create_artifact(
        self, name_or_power: Optional[Union[str, int]] = None
    ) -> Card:
        """Create an artifact card.

        Args:
            name_or_power: Name or power level for the artifact.

        Returns:
            A Card instance.
        """
        ...

    @abstractmethod
    def create_themed_deck(self, size: int) -> Dict:
        """Create a themed deck of the given size.

        Args:
            size: Number of cards in the deck.

        Returns:
            A dict of cards.
        """
        ...

    @abstractmethod
    def get_supported_types(self) -> Dict:
        """Return the supported card types.

        Returns:
            A dict listing supported types.
        """
        ...
