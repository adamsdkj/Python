"""FantasyCardFactory module for creating fantasy-themed cards."""

import random
from typing import Dict, Optional, Union

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    """Factory for creating fantasy-themed cards."""

    def __init__(self) -> None:
        """Initialize the factory with zero created cards."""
        self.created: int = 0

    def create_creature(
        self, name_or_power: Optional[Union[str, int]] = None
    ) -> Optional[Card]:
        """Create a creature card.

        Args:
            name_or_power: Name or power level for the creature.

        Returns:
            A CreatureCard instance, or None if invalid input.
        """
        if isinstance(name_or_power, str):
            self.created += 1
            return CreatureCard(
                name_or_power, 5, 'legendary', 5, 10
            )
        elif isinstance(name_or_power, int):
            self.created += 1
            return CreatureCard(
                'dragon', 5, 'legendary', name_or_power, 10
            )
        else:
            return None

    def create_spell(
        self, name_or_power: Optional[Union[str, int]] = None
    ) -> Optional[Card]:
        """Create a spell card.

        Args:
            name_or_power: Name or power level for the spell.

        Returns:
            A SpellCard instance, or None if invalid input.
        """
        if isinstance(name_or_power, str):
            self.created += 1
            return SpellCard(
                name_or_power, 3, 'rare', 7,
                "deals 3 damage to target"
            )
        elif isinstance(name_or_power, int):
            self.created += 1
            return SpellCard(
                'fireball', 3, 'rare', name_or_power,
                "deals 3 damage to target"
            )
        else:
            return None

    def create_artifact(
        self, name_or_power: Optional[Union[str, int]] = None
    ) -> Optional[Card]:
        """Create an artifact card.

        Args:
            name_or_power: Name or power level for the artifact.

        Returns:
            An ArtifactCard instance, or None if invalid input.
        """
        if isinstance(name_or_power, str):
            self.created += 1
            return ArtifactCard(
                name_or_power, 2, 'uncommon', 5,
                "Permanent: +1 mana per turn"
            )
        elif isinstance(name_or_power, int):
            self.created += 1
            return ArtifactCard(
                'mana_ring', 2, 'uncommon', name_or_power,
                "Permanent: +1 mana per turn"
            )
        else:
            return None

    def create_themed_deck(self, size: int) -> Dict:
        """Create a themed deck of the given size.

        Args:
            size: Number of cards in the deck.

        Returns:
            A dict of cards keyed by index.
        """
        cards = [
            self.create_artifact,
            self.create_creature,
            self.create_artifact,
        ]
        result: Dict = {}
        for i in range(0, size):
            result.update({f'{i}': random.choice(cards)(2)})
        return result

    def get_supported_types(self) -> Dict:
        """Return the supported card types.

        Returns:
            A dict listing supported creature, spell and artifact types.
        """
        result: Dict = {
            'creatures': ['dragon', 'goblin'],
            'spells': ['fireball'],
            'artifacts': ['mana_ring'],
        }
        return result
