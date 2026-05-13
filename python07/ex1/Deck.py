#! /usr/bin/env python3
"""Deck module for managing collections of cards."""

import random
from typing import Dict, Optional

from ex0.Card import Card
from enum import Enum


class CardType(Enum):
    """Enumeration of supported card types."""

    CREATURECARD = "CreatureCard"
    SPELLCARD = "SpellCard"
    ARTIFACTCARD = "ArtifactCard"


class Deck:
    """A deck that holds and manages a collection of cards."""

    def add_card(self, card: Card) -> None:
        """Add a card to the deck.

        Args:
            card: The card to add.
        """
        if not hasattr(self, "cards"):
            self.cards = list()
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """Remove a card from the deck by name.

        Args:
            card_name: The name of the card to remove.

        Returns:
            True if the card was found and removed, False otherwise.
        """
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        """Shuffle the deck randomly."""
        random.shuffle(self.cards)

    def draw_card(self) -> Optional[Card]:
        """Draw the top card from the deck.

        Returns:
            The top card, or None if the deck is empty.
        """
        if self.cards:
            return self.cards.pop(0)
        else:
            return None

    def get_deck_stats(self) -> dict:
        """Calculate and return statistics about the deck.

        Returns:
            A dict with total cards, type counts, and average cost.
        """
        result: Dict = {
            "total_cards": len(self.cards),
            "creature_cards": 0,
            "artifact_cards": 0,
            "spell_cards": 0,
            "avg_cost": 0,
        }
        total, count = 0, 0
        for card in self.cards:
            class_name = card.__class__.__name__
            if class_name == CardType.CREATURECARD.value:
                result["creature_cards"] += 1
            elif class_name == CardType.ARTIFACTCARD.value:
                result["artifact_cards"] += 1
            elif class_name == CardType.SPELLCARD.value:
                result["spell_cards"] += 1
            count += 1
            total += card.cost
        result["avg_cost"] = (total // count) if count > 0 else 0
        return result
