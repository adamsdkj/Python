#!/usr/bin/env python3
"""Card module providing the abstract base class for all cards."""

from abc import ABC, abstractmethod
from typing import Dict


class Card(ABC):
    """Abstract base class representing a generic card."""

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        """Initialize a Card.

        Args:
            name: The name of the card.
            cost: The mana cost of the card.
            rarity: The rarity level of the card.
        """
        self.name: str = name
        self.cost: int = cost
        self.rarity: str = rarity

    @abstractmethod
    def play(self, game_state: Dict) -> Dict:
        """Play the card given a game state.

        Args:
            game_state: Current state of the game.

        Returns:
            A dict describing the result of playing the card.
        """
        ...

    def get_card_info(self) -> Dict:
        """Return basic card information as a dictionary.

        Returns:
            A dict with name, cost and rarity.
        """
        card_info = {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
        }
        return card_info

    def is_playable(self, available_mana: int) -> bool:
        """Check whether the card can be played with available mana.

        Args:
            available_mana: The amount of mana currently available.

        Returns:
            True if the card cost is less than available mana.
        """
        if self.cost < available_mana:
            return True
        return False
