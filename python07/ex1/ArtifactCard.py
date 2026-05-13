#! /usr/bin/env python3
"""ArtifactCard module for artifact-type cards."""

from typing import Dict, List

from ex0.Card import Card


class ArtifactCard(Card):
    """A card representing an artifact with durability and effect."""

    def __init__(
        self, name: str, cost: int, rarity: str,
        durability: int, effect: str
    ) -> None:
        """Initialize an ArtifactCard.

        Args:
            name: The name of the artifact.
            cost: The mana cost to play.
            rarity: The rarity level.
            durability: How durable the artifact is.
            effect: Description of the artifact's effect.

        Raises:
            ValueError: If cost or durability is negative.
        """
        if (cost or durability) < 0:
            raise ValueError(
                "ArtifactCard: A negative number is not valid"
            )
        super().__init__(name, cost, rarity)
        self.rarity = rarity
        self.effect = effect
        self.durability = durability

    def play(self, game_state: Dict) -> Dict:
        """Play the artifact card given a game state.

        Args:
            game_state: Current state of the game.

        Returns:
            A dict describing the result of playing the card.
        """
        if game_state.get('mana') < self.cost:
            return {'error': 'Not enough mana to play this card.'}
        result: Dict = {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self.effect,
        }
        return result

    def resolve_effect(self, targets: List) -> Dict:
        """Resolve the artifact's effect on targets.

        Args:
            targets: List of targets for the effect.

        Returns:
            A dict describing the resolved effect.
        """
        return {}

    def __str__(self) -> str:
        """Return string representation of the artifact card."""
        return "(Artifact)"
